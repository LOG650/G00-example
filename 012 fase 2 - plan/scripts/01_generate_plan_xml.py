#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.14"
# dependencies = []
# ///

from __future__ import annotations

import argparse
import json
import subprocess
from dataclasses import dataclass, field
from datetime import date, datetime, time
from pathlib import Path
from typing import Any
import xml.etree.ElementTree as ET
from xml.dom import minidom

NS = "http://schemas.microsoft.com/project/2007"
ET.register_namespace("", NS)

WORK_START = time(8, 0, 0)
LUNCH_START = time(12, 0, 0)
LUNCH_END = time(13, 0, 0)
WORK_END = time(17, 0, 0)
MINUTES_PER_DAY = 8 * 60
MINUTES_PER_WEEK = 5 * MINUTES_PER_DAY
DAYS_PER_MONTH = 20
DEFAULT_DURATION_FORMAT_DAYS = 7
LINK_TYPE_MAP = {
    "finish-to-finish": 0,
    "finish-to-start": 1,
    "start-to-finish": 2,
    "start-to-start": 3,
}
DAY_TYPE_MAP = {
    "sunday": 1,
    "monday": 2,
    "tuesday": 3,
    "wednesday": 4,
    "thursday": 5,
    "friday": 6,
    "saturday": 7,
}
DAY_NAME_TO_WEEKDAY = {
    "monday": 0,
    "tuesday": 1,
    "wednesday": 2,
    "thursday": 3,
    "friday": 4,
    "saturday": 5,
    "sunday": 6,
}


@dataclass
class TaskTiming:
    planned_start: date
    planned_finish: date
    baseline_start: date
    baseline_finish: date
    start_dt: datetime
    finish_dt: datetime
    duration_minutes: int
    percent_complete: int
    actual_start_dt: datetime | None
    actual_finish_dt: datetime | None
    actual_duration_minutes: int | None
    remaining_duration_minutes: int


@dataclass
class TaskNode:
    name: str
    notes: str
    outline_level: int
    outline_number: str
    wbs_code: str
    summary: bool
    milestone: bool
    critical: bool
    calendar_uid: int
    timing: TaskTiming
    activity_id: str | None = None
    predecessors: list[dict[str, Any]] = field(default_factory=list)
    children: list["TaskNode"] = field(default_factory=list)
    uid: int = 0
    task_id: int = 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generer Microsoft Project MSPDI plan.xml fra LOG650-planfiler."
    )
    parser.add_argument(
        "--plan-dir",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="Katalogen som inneholder core.json, schedule.json, wbs.json, requirements.json og risk.json.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Utdatafil. Standard er <plan-dir>/plan.xml.",
    )
    parser.add_argument(
        "--no-git-fallback",
        action="store_true",
        help="Ikke bruk git-historikk til å fylle inn faktiske datoer som mangler i JSON.",
    )
    return parser.parse_args()


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def parse_date(value: str) -> date:
    if "T" in value:
        value = value.split("T", 1)[0]
    return date.fromisoformat(value)


def start_of_day(day: date) -> datetime:
    return datetime.combine(day, WORK_START)


def finish_of_day(day: date) -> datetime:
    return datetime.combine(day, WORK_END)


def iso_datetime(value: datetime | None) -> str | None:
    if value is None:
        return None
    return value.strftime("%Y-%m-%dT%H:%M:%S")


def minutes_to_duration(total_minutes: int) -> str:
    total_minutes = max(0, int(round(total_minutes)))
    hours, minutes = divmod(total_minutes, 60)
    return f"PT{hours}H{minutes}M0S"


def working_days_inclusive(start_day: date, finish_day: date, working_weekdays: set[int]) -> int:
    if finish_day < start_day:
        return 0
    count = 0
    current = start_day
    while current <= finish_day:
        if current.weekday() in working_weekdays:
            count += 1
        current = current.fromordinal(current.toordinal() + 1)
    return count


def duration_minutes_between(start_day: date, finish_day: date, working_weekdays: set[int]) -> int:
    return working_days_inclusive(start_day, finish_day, working_weekdays) * MINUTES_PER_DAY


def weighted_percent(children: list[TaskNode]) -> int:
    total = sum(child.timing.duration_minutes for child in children)
    if total <= 0:
        return 0
    weighted = sum(child.timing.duration_minutes * child.timing.percent_complete for child in children)
    return int(round(weighted / total))


def add_text(parent: ET.Element, name: str, value: Any) -> ET.Element | None:
    if value is None:
        return None
    element = ET.SubElement(parent, f"{{{NS}}}{name}")
    if isinstance(value, bool):
        element.text = str(value).lower()
    else:
        element.text = str(value)
    return element


def sort_code(code: str) -> tuple[int, ...]:
    return tuple(int(part) for part in code.split("."))


def git_repo_root(plan_dir: Path) -> Path | None:
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--show-toplevel"],
            cwd=plan_dir,
            capture_output=True,
            check=True,
            text=True,
        )
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None
    return Path(result.stdout.strip())


def git_dates_for_activity(repo_root: Path | None, task_id: str, plan_dir: Path) -> tuple[date | None, date | None]:
    if repo_root is None:
        return None, None

    prefix = task_id.replace(".", "_")
    candidates: list[Path] = []

    activities_dir = repo_root / "006 analysis" / "aktiviteter"
    if activities_dir.exists():
        for directory in activities_dir.glob(f"{prefix}_*"):
            if not directory.is_dir():
                continue
            files = [
                path
                for path in directory.rglob("*")
                if path.is_file() and path.name.lower() != "readme.md"
            ]
            candidates.extend(files)

    reviews_dir = plan_dir / "reviews"
    if reviews_dir.exists():
        candidates.extend(path for path in reviews_dir.glob(f"{prefix}_*") if path.exists())

    if not candidates:
        return None, None

    try:
        result = subprocess.run(
            ["git", "log", "--date=short", "--format=%ad", "--", *[str(path) for path in candidates]],
            cwd=repo_root,
            capture_output=True,
            check=True,
            text=True,
        )
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None, None

    dates = [parse_date(line.strip()) for line in result.stdout.splitlines() if line.strip()]
    if not dates:
        return None, None
    return min(dates), max(dates)


def actual_dates_for_activity(
    activity: dict[str, Any],
    plan_dir: Path,
    repo_root: Path | None,
    use_git_fallback: bool,
) -> tuple[datetime | None, datetime | None]:
    execution = activity.get("execution", {})
    started_raw = execution.get("startedAt")
    completed_raw = execution.get("completedAt")

    if started_raw:
        actual_start = start_of_day(parse_date(started_raw))
    else:
        actual_start = None

    if completed_raw:
        actual_finish = finish_of_day(parse_date(completed_raw))
    else:
        actual_finish = None

    git_start = git_finish = None
    if use_git_fallback:
        git_start, git_finish = git_dates_for_activity(repo_root, activity["taskId"], plan_dir)

    planned_start = parse_date(activity["plannedStart"])
    planned_finish = parse_date(activity["plannedFinish"])
    status = activity.get("status", "")
    percent = int(activity.get("percentComplete", 0))

    if actual_start is None:
        if git_start is not None and (status == "completed" or percent > 0):
            actual_start = start_of_day(git_start)
        elif status == "completed":
            actual_start = start_of_day(planned_start)
        elif percent > 0:
            actual_start = start_of_day(planned_start)

    if actual_finish is None and status == "completed":
        if git_finish is not None:
            actual_finish = finish_of_day(git_finish)
        else:
            actual_finish = finish_of_day(planned_finish)

    return actual_start, actual_finish


def leaf_timing(
    activity: dict[str, Any],
    plan_dir: Path,
    repo_root: Path | None,
    working_weekdays: set[int],
    use_git_fallback: bool,
) -> TaskTiming:
    planned_start = parse_date(activity["plannedStart"])
    planned_finish = parse_date(activity["plannedFinish"])
    duration_minutes = duration_minutes_between(planned_start, planned_finish, working_weekdays)
    percent = int(activity.get("percentComplete", 0))
    actual_start, actual_finish = actual_dates_for_activity(activity, plan_dir, repo_root, use_git_fallback)

    actual_duration = None
    if actual_start and actual_finish:
        actual_duration = duration_minutes_between(actual_start.date(), actual_finish.date(), working_weekdays)

    remaining_duration = 0 if percent >= 100 else int(round(duration_minutes * (100 - percent) / 100))

    return TaskTiming(
        planned_start=planned_start,
        planned_finish=planned_finish,
        baseline_start=planned_start,
        baseline_finish=planned_finish,
        start_dt=start_of_day(planned_start),
        finish_dt=finish_of_day(planned_finish),
        duration_minutes=duration_minutes,
        percent_complete=percent,
        actual_start_dt=actual_start,
        actual_finish_dt=actual_finish,
        actual_duration_minutes=actual_duration,
        remaining_duration_minutes=remaining_duration,
    )


def summary_timing(children: list[TaskNode], working_weekdays: set[int]) -> TaskTiming:
    start_day = min(child.timing.planned_start for child in children)
    finish_day = max(child.timing.planned_finish for child in children)
    baseline_start = min(child.timing.baseline_start for child in children)
    baseline_finish = max(child.timing.baseline_finish for child in children)
    percent = weighted_percent(children)

    actual_starts = [child.timing.actual_start_dt for child in children if child.timing.actual_start_dt]
    actual_finishes = [child.timing.actual_finish_dt for child in children if child.timing.actual_finish_dt]
    actual_start = min(actual_starts) if actual_starts else None
    actual_finish = max(actual_finishes) if len(actual_finishes) == len(children) else None

    actual_duration = None
    if actual_start and actual_finish:
        actual_duration = duration_minutes_between(actual_start.date(), actual_finish.date(), working_weekdays)

    remaining_duration = sum(child.timing.remaining_duration_minutes for child in children)

    return TaskTiming(
        planned_start=start_day,
        planned_finish=finish_day,
        baseline_start=baseline_start,
        baseline_finish=baseline_finish,
        start_dt=start_of_day(start_day),
        finish_dt=finish_of_day(finish_day),
        duration_minutes=duration_minutes_between(start_day, finish_day, working_weekdays),
        percent_complete=percent,
        actual_start_dt=actual_start,
        actual_finish_dt=actual_finish,
        actual_duration_minutes=actual_duration,
        remaining_duration_minutes=remaining_duration,
    )


def build_task_tree(
    root_item_id: str,
    wbs_items: dict[str, dict[str, Any]],
    children_by_parent: dict[str | None, list[dict[str, Any]]],
    activities_by_id: dict[str, dict[str, Any]],
    plan_dir: Path,
    repo_root: Path | None,
    working_weekdays: set[int],
    use_git_fallback: bool,
) -> TaskNode:
    item = wbs_items[root_item_id]
    children_items = children_by_parent.get(root_item_id, [])
    child_nodes = [
        build_task_tree(
            child["wbsItemId"],
            wbs_items,
            children_by_parent,
            activities_by_id,
            plan_dir,
            repo_root,
            working_weekdays,
            use_git_fallback,
        )
        for child in children_items
    ]

    direct_activities = [
        activities_by_id[activity_id]
        for activity_id in item.get("activityIds", [])
        if activity_id in activities_by_id and activities_by_id[activity_id]["wbsItemId"] == item["wbsItemId"]
    ]

    if child_nodes:
        timing = summary_timing(child_nodes, working_weekdays)
        return TaskNode(
            name=item["name"],
            notes=f"WBS: {item['code']}\nKilde: {item['wbsItemId']}\nStatus: {item.get('status', '')}\nBeskrivelse: {item.get('description', '')}",
            outline_level=int(item["level"]),
            outline_number=item["code"],
            wbs_code=item["code"],
            summary=True,
            milestone=False,
            critical=any(child.critical for child in child_nodes),
            calendar_uid=1,
            timing=timing,
            children=child_nodes,
        )

    if len(direct_activities) == 1:
        activity = direct_activities[0]
        timing = leaf_timing(activity, plan_dir, repo_root, working_weekdays, use_git_fallback)
        notes = (
            f"WBS: {item['code']} ({item['wbsItemId']})\n"
            f"Aktivitet: {activity['activityId']} / {activity['taskId']}\n"
            f"WBS-beskrivelse: {item.get('description', '')}\n"
            f"Aktivitetsbeskrivelse: {activity.get('description', '')}\n"
            f"Status: {activity.get('status', '')}\n"
            f"Siste hendelse: {activity.get('execution', {}).get('lastEvent') or ''}"
        )
        return TaskNode(
            name=activity["name"],
            notes=notes,
            outline_level=int(item["level"]),
            outline_number=item["code"],
            wbs_code=item["code"],
            summary=False,
            milestone=timing.planned_start == timing.planned_finish,
            critical=bool(activity.get("isCriticalPath")),
            calendar_uid=1,
            timing=timing,
            activity_id=activity["activityId"],
            predecessors=activity.get("predecessors", []),
        )

    if len(direct_activities) > 1:
        child_nodes = []
        for index, activity in enumerate(sorted(direct_activities, key=lambda value: value["taskId"]), start=1):
            timing = leaf_timing(activity, plan_dir, repo_root, working_weekdays, use_git_fallback)
            child_nodes.append(
                TaskNode(
                    name=activity["name"],
                    notes=(
                        f"WBS: {item['code']} ({item['wbsItemId']})\n"
                        f"Aktivitet: {activity['activityId']} / {activity['taskId']}\n"
                        f"Aktivitetsbeskrivelse: {activity.get('description', '')}"
                    ),
                    outline_level=int(item["level"]) + 1,
                    outline_number=f"{item['code']}.{index}",
                    wbs_code=f"{item['code']}.{index}",
                    summary=False,
                    milestone=timing.planned_start == timing.planned_finish,
                    critical=bool(activity.get("isCriticalPath")),
                    calendar_uid=1,
                    timing=timing,
                    activity_id=activity["activityId"],
                    predecessors=activity.get("predecessors", []),
                )
            )
        timing = summary_timing(child_nodes, working_weekdays)
        return TaskNode(
            name=item["name"],
            notes=f"WBS: {item['code']}\nKilde: {item['wbsItemId']}\nBeskrivelse: {item.get('description', '')}",
            outline_level=int(item["level"]),
            outline_number=item["code"],
            wbs_code=item["code"],
            summary=True,
            milestone=False,
            critical=any(child.critical for child in child_nodes),
            calendar_uid=1,
            timing=timing,
            children=child_nodes,
        )

    timing = TaskTiming(
        planned_start=date.today(),
        planned_finish=date.today(),
        baseline_start=date.today(),
        baseline_finish=date.today(),
        start_dt=start_of_day(date.today()),
        finish_dt=finish_of_day(date.today()),
        duration_minutes=0,
        percent_complete=0,
        actual_start_dt=None,
        actual_finish_dt=None,
        actual_duration_minutes=None,
        remaining_duration_minutes=0,
    )
    return TaskNode(
        name=item["name"],
        notes=f"WBS: {item['code']}\nKilde: {item['wbsItemId']}\nBeskrivelse: {item.get('description', '')}",
        outline_level=int(item["level"]),
        outline_number=item["code"],
        wbs_code=item["code"],
        summary=False,
        milestone=False,
        critical=False,
        calendar_uid=1,
        timing=timing,
    )


def flatten_tasks(root: TaskNode) -> list[TaskNode]:
    ordered: list[TaskNode] = []

    def visit(node: TaskNode) -> None:
        ordered.append(node)
        for child in node.children:
            visit(child)

    visit(root)
    for index, node in enumerate(ordered, start=1):
        node.uid = index
        node.task_id = index
    return ordered


def add_task_xml(parent: ET.Element, node: TaskNode, activity_to_uid: dict[str, int]) -> None:
    task_el = ET.SubElement(parent, f"{{{NS}}}Task")
    add_text(task_el, "UID", node.uid)
    add_text(task_el, "ID", node.task_id)
    add_text(task_el, "Name", node.name)
    add_text(task_el, "WBS", node.wbs_code)
    add_text(task_el, "OutlineNumber", node.outline_number)
    add_text(task_el, "OutlineLevel", node.outline_level)
    add_text(task_el, "Start", iso_datetime(node.timing.start_dt))
    add_text(task_el, "Finish", iso_datetime(node.timing.finish_dt))
    add_text(task_el, "Duration", minutes_to_duration(node.timing.duration_minutes))
    add_text(task_el, "DurationFormat", DEFAULT_DURATION_FORMAT_DAYS)
    add_text(task_el, "Manual", False)
    add_text(task_el, "Summary", node.summary)
    add_text(task_el, "Milestone", node.milestone)
    add_text(task_el, "Critical", node.critical)
    add_text(task_el, "CalendarUID", node.calendar_uid)
    add_text(task_el, "PercentComplete", node.timing.percent_complete)
    add_text(task_el, "PercentWorkComplete", node.timing.percent_complete)
    add_text(task_el, "ActualStart", iso_datetime(node.timing.actual_start_dt))
    add_text(task_el, "ActualFinish", iso_datetime(node.timing.actual_finish_dt))
    if node.timing.actual_duration_minutes is not None:
        add_text(task_el, "ActualDuration", minutes_to_duration(node.timing.actual_duration_minutes))
    add_text(task_el, "RemainingDuration", minutes_to_duration(node.timing.remaining_duration_minutes))
    add_text(task_el, "Notes", node.notes)

    if not node.summary and node.predecessors:
        for predecessor in node.predecessors:
            predecessor_uid = activity_to_uid.get(predecessor["activityId"])
            if predecessor_uid is None:
                continue
            link_el = ET.SubElement(task_el, f"{{{NS}}}PredecessorLink")
            add_text(link_el, "PredecessorUID", predecessor_uid)
            add_text(link_el, "Type", LINK_TYPE_MAP.get(predecessor.get("type", "finish-to-start"), 1))
            add_text(link_el, "LinkLag", int(predecessor.get("lagDays", 0)) * MINUTES_PER_DAY * 10)
            add_text(link_el, "LagFormat", DEFAULT_DURATION_FORMAT_DAYS)

    baseline_el = ET.SubElement(task_el, f"{{{NS}}}Baseline")
    add_text(baseline_el, "Number", 0)
    add_text(baseline_el, "Interim", False)
    add_text(baseline_el, "Start", iso_datetime(start_of_day(node.timing.baseline_start)))
    add_text(baseline_el, "Finish", iso_datetime(finish_of_day(node.timing.baseline_finish)))
    add_text(baseline_el, "Duration", minutes_to_duration(node.timing.duration_minutes))
    add_text(baseline_el, "DurationFormat", DEFAULT_DURATION_FORMAT_DAYS)


def add_calendar_xml(parent: ET.Element, calendar_name: str, working_days: list[str]) -> None:
    calendars_el = ET.SubElement(parent, f"{{{NS}}}Calendars")
    calendar_el = ET.SubElement(calendars_el, f"{{{NS}}}Calendar")
    add_text(calendar_el, "UID", 1)
    add_text(calendar_el, "Name", calendar_name)
    add_text(calendar_el, "IsBaseCalendar", True)

    working_weekdays = {DAY_NAME_TO_WEEKDAY[name] for name in working_days}

    weekdays_el = ET.SubElement(calendar_el, f"{{{NS}}}WeekDays")
    for day_name, day_type in DAY_TYPE_MAP.items():
        weekday_el = ET.SubElement(weekdays_el, f"{{{NS}}}WeekDay")
        add_text(weekday_el, "DayType", day_type)
        is_working = DAY_NAME_TO_WEEKDAY[day_name] in working_weekdays
        add_text(weekday_el, "DayWorking", is_working)
        if not is_working:
            continue
        working_times_el = ET.SubElement(weekday_el, f"{{{NS}}}WorkingTimes")
        first = ET.SubElement(working_times_el, f"{{{NS}}}WorkingTime")
        add_text(first, "FromTime", WORK_START.strftime("%H:%M:%S"))
        add_text(first, "ToTime", LUNCH_START.strftime("%H:%M:%S"))
        second = ET.SubElement(working_times_el, f"{{{NS}}}WorkingTime")
        add_text(second, "FromTime", LUNCH_END.strftime("%H:%M:%S"))
        add_text(second, "ToTime", WORK_END.strftime("%H:%M:%S"))


def prettify_xml(root: ET.Element) -> bytes:
    raw = ET.tostring(root, encoding="utf-8")
    pretty = minidom.parseString(raw).toprettyxml(indent="  ", encoding="utf-8")
    return pretty


def main() -> None:
    args = parse_args()
    plan_dir = args.plan_dir.resolve()
    output_path = args.output.resolve() if args.output else plan_dir / "plan.xml"

    required = {
        "core": plan_dir / "core.json",
        "schedule": plan_dir / "schedule.json",
        "wbs": plan_dir / "wbs.json",
        "requirements": plan_dir / "requirements.json",
        "risk": plan_dir / "risk.json",
    }
    missing = [str(path) for path in required.values() if not path.exists()]
    if missing:
        raise SystemExit(f"Mangler planfiler: {', '.join(missing)}")

    core = load_json(required["core"])
    schedule = load_json(required["schedule"])
    wbs = load_json(required["wbs"])
    load_json(required["requirements"])
    load_json(required["risk"])

    project = core["project"]
    schedule_data = schedule["schedule"]
    wbs_data = wbs["wbs"]

    calendar = schedule_data["calendars"][0]
    working_days = calendar.get("workingDays") or ["monday", "tuesday", "wednesday", "thursday", "friday"]
    working_weekdays = {DAY_NAME_TO_WEEKDAY[name] for name in working_days}
    repo_root = None if args.no_git_fallback else git_repo_root(plan_dir)

    activities = {activity["activityId"]: activity for activity in schedule_data["activities"]}
    wbs_items = {item["wbsItemId"]: item for item in wbs_data["items"]}

    children_by_parent: dict[str | None, list[dict[str, Any]]] = {}
    for item in wbs_data["items"]:
        children_by_parent.setdefault(item.get("parentId"), []).append(item)
    for siblings in children_by_parent.values():
        siblings.sort(key=lambda item: sort_code(item["code"]))

    root_task = build_task_tree(
        wbs_data["items"][0]["wbsItemId"],
        wbs_items,
        children_by_parent,
        activities,
        plan_dir,
        repo_root,
        working_weekdays,
        not args.no_git_fallback,
    )
    tasks = flatten_tasks(root_task)
    activity_to_uid = {task.activity_id: task.uid for task in tasks if task.activity_id}

    project_el = ET.Element(f"{{{NS}}}Project")
    add_text(project_el, "SaveVersion", 12)
    add_text(project_el, "UID", "1")
    add_text(project_el, "Name", project["name"])
    add_text(project_el, "Title", project["name"])
    add_text(project_el, "Subject", project.get("description"))
    add_text(project_el, "Company", project.get("governance", {}).get("ownerOrganization"))
    add_text(project_el, "Manager", project.get("governance", {}).get("projectManager", {}).get("name"))
    add_text(project_el, "Author", project.get("governance", {}).get("technicalLead", {}).get("name"))
    add_text(project_el, "CreationDate", project.get("audit", {}).get("createdAt"))
    add_text(project_el, "LastSaved", project.get("audit", {}).get("updatedAt"))
    add_text(project_el, "ScheduleFromStart", True)
    add_text(project_el, "StartDate", iso_datetime(start_of_day(root_task.timing.planned_start)))
    add_text(project_el, "CalendarUID", 1)
    add_text(project_el, "DefaultStartTime", WORK_START.strftime("%H:%M:%S"))
    add_text(project_el, "DefaultFinishTime", WORK_END.strftime("%H:%M:%S"))
    add_text(project_el, "MinutesPerDay", MINUTES_PER_DAY)
    add_text(project_el, "MinutesPerWeek", MINUTES_PER_WEEK)
    add_text(project_el, "DaysPerMonth", DAYS_PER_MONTH)
    add_text(project_el, "DefaultTaskType", 1)

    add_calendar_xml(project_el, calendar["name"], working_days)

    tasks_el = ET.SubElement(project_el, f"{{{NS}}}Tasks")
    for task in tasks:
        add_task_xml(tasks_el, task, activity_to_uid)

    ET.SubElement(project_el, f"{{{NS}}}Resources")
    ET.SubElement(project_el, f"{{{NS}}}Assignments")

    output_path.write_bytes(prettify_xml(project_el))
    print(f"Skrev MSPDI-fil til {output_path}")


if __name__ == "__main__":
    main()
