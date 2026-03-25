---
name: handoff
description: >-
  Lag et strukturert overleveringsdokument som fanger opp nåværende status
  slik at neste sesjon kan fortsette sømløst. Triggeres av «handoff»,
  «overlevering» eller «/handoff».
allowed-tools: Read, Glob, Grep, Bash, Write
---

# Handoff: Overleveringsdokument for PowerHorse-prosjektet

## Mål

Lag et kompakt overleveringsdokument som fanger opp alt neste sesjon trenger for å fortsette arbeidet uten oppstartsfriksjon. Eksternaliser sesjonens kontekst til en persistent fil — bare det essensielle.

## Når brukes denne skillen

- Før en lang sesjon avsluttes og arbeidet skal fortsette senere.
- Før kontekstvinduet fylles opp (proaktivt, ikke reaktivt).
- Ved faseskifte (f.eks. fra analyse til rapportskriving).
- Ved overlevering mellom sesjoner.

## Prosess

### 1. Analyser nåværende sesjon

Gå gjennom samtalen og svar på:

- Hva var den opprinnelige oppgaven?
- Hva er fullført?
- Hva er pågående eller blokkert?
- Hvilke nøkkelbeslutninger ble tatt og hvorfor?
- Hvilke filer ble lest, opprettet eller endret?
- Hvilke blindveier ble utforsket (slik at neste sesjon unngår dem)?

### 2. Hent inn nåværende tilstand

```bash
git status --short
git diff --stat HEAD
git log --oneline -5
git branch --show-current
```

Sjekk også:

- `012 fase 2 - plan/status.md` — for prosjektstatus
- Eventuelle ucommittede endringer i rapport eller analysefiler

### 3. Skriv overleveringsdokumentet

Lagre til `HANDOFF.md` i prosjektroten.

Bruk denne strukturen:

```markdown
# Handoff: [Kort oppgavebeskrivelse]

**Dato:** [dato]
**Branch:** [branch]
**Siste commit:** [hash + melding, eller «ucommittede endringer»]

## Mål

[1–2 setninger: hva vi prøver å oppnå. Referer til aktivitet/krav fra prosjektplanen hvis relevant.]

## Fullført

- [x] [Oppgave — kort beskrivelse av hva som ble gjort]
- [x] [Oppgave — kort beskrivelse]

## Neste steg

- [ ] [Oppgave — hva som må gjøres, med filbaner og konkrete detaljer]
- [ ] [Oppgave — eventuelle blokkeringer med forklaring]

## Nøkkelbeslutninger

Dokumenter HVORFOR valg ble tatt, ikke bare hva:

- **[Beslutning]**: [Valg] — [Begrunnelse, inkl. forkastede alternativer]

## Blindveier (ikke gjenta disse)

- [Tilnærming som ble prøvd] — [Hvorfor den ikke fungerte]

## Endrede filer

- `sti/til/fil` — [hva som ble endret og hvorfor, 1 linje]
- `sti/til/ny-fil` — [NY: hva filen gjør]

## Prosjektstatus

- **Aktivitet under arbeid:** [ACT-X.Y — navn og status]
- **Rapportstatus:** [hvilke kapitler som er oppdatert/mangler]
- **Plan/status synkronisert:** [ja/nei — hva mangler]
- **Ucommittede endringer:** [ja/nei — hva]

## Kontekst for neste sesjon

[2–4 setninger: det VIKTIGSTE neste sesjon må vite. Hva er situasjonen? Hva er største risiko? Hva bør gjøres først?]

**Anbefalt første handling:** [Konkret steg å starte med]
```

### 4. Bekreft og gi råd

Etter at dokumentet er skrevet:

1. Bekreft at filen ble skrevet med full filbane.
2. Foreslå at neste sesjon starter med:
   ```
   Les HANDOFF.md og fortsett fra der forrige sesjon slapp.
   ```
3. Hvis det finnes ucommittede endringer, foreslå å committe først.

## Kvalitetskriterier

Et godt overleveringsdokument skal:

- La en ny sesjon fortsette uten oppklaringsspørsmål.
- Være under 100 linjer — konsist, ikke uttømmende. Referer til filer i stedet for å kopiere innhold.
- Inkludere nok «hvorfor»-kontekst til at neste sesjon tar de samme valgene.
- Eksplisitt liste blindveier for å unngå gjentatt arbeid.
- Ha en konkret «første handling»-anbefaling.
- Knytte arbeidet til prosjektplanens aktiviteter og krav der det er relevant.

## Antipatterns

- Ikke inkluder fullt filinnhold — referer til filbaner.
- Ikke inkluder samtalehistorikk — oppsummer funn.
- Ikke vær vag («fiks rapporten») — vær spesifikk («oppdater seksjon 7.1 i `005 report/rapport.md` med residualanalyse fra `006 analysis/aktiviteter/3_3_validere_modell/`»).
- Ikke hopp over «Blindveier»-seksjonen — den forhindrer mest bortkastet tid.
- Ikke glem «Nøkkelbeslutninger» — uten den kan neste sesjon reversere valgene dine.
- Ikke glem å sjekke om `status.md` og planfiler er oppdatert.
