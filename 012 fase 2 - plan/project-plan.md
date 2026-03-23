# Prosjektstyringsplan

for

PowerHorse-prosjektet

2026-02-13

Utarbeidet av:
Prosjektgruppen

Autorisert av:
Emneansvarlig LOG650

## Sammendrag

Dette dokumentet utgjor prosjektstyringsplanen for PowerHorse-prosjektet i LOG650. Planen dokumenterer baseline for omfang, fremdrift, risiko, kvalitet og enkel ressursbruk for et studentprosjekt som skal utvikle en kvantitativ modell for manedlig ettersporselsprognose av traktorsalg. Prosjektet bygger pa proposalen fra fase 1 og brukes som styringsgrunnlag for fase 2, 3 og 4.

Prosjektet stotter emnets mal om a bruke kvantitative metoder i logistikk pa et konkret case. Dokumentet er et levende styringsdokument og skal oppdateres ved vesentlige endringer i omfang, fremdrift eller risiko.

## Behov

Casebedriften PowerHorse har behov for bedre prognoser for manedlig traktorsalg. Ettersporselen viser bade trend og tydelig sesongvariasjon, og svak prognoseevne gir risiko for feil produksjonsniva, unodvendig lager og svak kapasitetsplanlegging. Prosjektet skal derfor utvikle en modell som gir et bedre grunnlag for produksjons- og lagerbeslutninger.

## Sponsor

Sponsor for prosjektet er emneansvarlig i LOG650. Sponsor har myndighet til a godkjenne proposal, plan og sluttleveranser i tråd med kursopplegget.

## Kunde

Kunden i prosjektet er primart den simulerte casebedriften PowerHorse. I praksis fungerer prosjektgruppen, faglaerer og medstudenter som representanter for kunden ved a vurdere om analysen er relevant, faglig forsvarlig og anvendbar for logistiske beslutninger.

## Forretningscase

Prosjektet er begrunnet fordi mer presise ettersporselsprognoser normalt gir bedre beslutninger i produksjonsplanlegging og lagerstyring. For dette caset betyr det at bedriften kan planlegge kapasitet tidligere, redusere risikoen for overproduksjon og unnga unodvendige lagerkostnader. For studentgruppen er prosjektet faglig relevant fordi det knytter sammen tidsserieanalyse, logistikk og beslutningsstotte.

## Alternativer

1. Ingen modellering, kun manuell vurdering av historiske data. Dette ble forkastet fordi det ikke gir en tilstrekkelig kvantitativ problemstilling.
2. En tidsseriemodell som handterer trend og sesong, eksempelvis SARIMA. Dette ble valgt fordi det passer direkte til casebeskrivelsen og datagrunnlaget.
3. En mer avansert modell med eksterne forklaringsvariabler. Dette ble forkastet i denne fasen fordi prosjektet mangler data om pris, kampanjer og marked, og fordi omfanget blir for stort for kursets tidsramme.

## Forutsetninger

- Caset og datasettet kan brukes som analysegrunnlag uten ny datainnsamling.
- Historiske data er tilstrekkelige til a analysere trend og sesong.
- Datakvaliteten antas a vaere kvalitetssjekket av de som leverte datasettet, siden prosjektet ikke har egne eksterne kilder for uavhengig validering av datakvalitet.
- Gruppen har tilgang til relevante verktoy og kan samarbeide via Teams og GitHub.
- Sluttleveranse kan styres mot en intern maldato 2026-05-15 siden eksakt fase-4-frist ikke er oppgitt i kursnotatet.

## Gevinster

For PowerHorse-caset er forventede gevinster bedre produksjonsplanlegging, bedre lageroppbygging mot hoysesong og et tydeligere bilde av usikkerheten i ettersporselen. For prosjektgruppen er gevinstene kompetanse i kvantitativ modellering, bedre faglig struktur og et sterkere grunnlag for rapport og presentasjon.

## Kostnader

Prosjektet har ikke et eget kontantbudsjett. Kostnaden bestar hovedsakelig av tidsbruk fra studentgruppen. Det planlegges heller ikke egne innkjop eller eksterne tjenester utover verktoy og infrastruktur som allerede er tilgjengelige gjennom emnet og prosjektets repositorium.

## Analyse

Sammenlignet med alternativene gir en avgrenset SARIMA-basert tilnaerming best balanse mellom faglig kvalitet, gjennomforbarhet og nytteverdi innenfor kursrammen. Losningen er derfor valgt som baseline for videre arbeid.

## Omfang

Prosjektet omfatter analyse av historiske manedlige salgsdata, datarensing, visualisering, valg og estimering av SARIMA-modell, modellvalidering og testsettvalidering, 12-maneders prognose og tolkning for logistiske beslutninger. Videre omfatter prosjektet alle styringsleveranser som kreves av emnet, inkludert proposal, prosjektplan, rapportutkast, peer review, presentasjon og endelig rapport.

Prosjektet omfatter ikke optimalisering av hele forsyningskjeden, kausale forklaringsvariabler som pris og markedsforing, eller implementering av losningen i et operativt system.

## Mål

Prosjektets hovedmal er a utvikle en kvantitativ og faglig forsvarlig prognosemodell for manedlig traktorsalg som kan brukes som beslutningsstotte i produksjons- og lagerplanlegging.

Prosjektets viktigste forutsetninger er:

- Case- og datagrunnlaget er tilgjengelig.
- Gruppen kan gjennomfore arbeid mellom samlingene.
- Emnets fasegodkjenninger oppnas som planlagt.

Prosjektets viktigste begrensninger er:

- All tekst skal skrives pa norsk.
- Problemstillingen ma vaere kvantitativ.
- Prosjektet ma folge kursfasene og samlingsdatoene.
- Prosjektet ma holde seg innenfor et studentprosjekts begrensede tid og datatilgang.

## Krav

| ID | Type | Krav | Eier | Leveranse | Verifikasjon |
| --- | --- | --- | --- | --- | --- |
| REQ-001 | Funksjonelt | Levere en 12-maneders prognose for traktorsalg | Analyseansvarlig | Prognosekapittel | Analyse |
| REQ-002 | Funksjonelt | Bruke historiske manedlige salgsdata som grunnlag | Dataansvarlig | Datagrunnlag | Review |
| REQ-003 | Funksjonelt | Velge en metode som handterer trend og sesong | Analyseansvarlig | Modellkapittel | Review |
| REQ-004 | Funksjonelt | Dokumentere modellvalidering | Analyseansvarlig | Kapittel 7, 8 og 9 | Analyse |
| REQ-005 | Funksjonelt | Oversette resultatene til logistiske anbefalinger | Prosjektgruppen | Diskusjon | Review |
| REQ-006 | Ikke-funksjonelt | Skrive alle leveranser pa norsk og holde sporbarhet mot proposal | Prosjektleder | Alle dokumenter | Review |
| REQ-007 | Ikke-funksjonelt | Levere i trad med kursfaser og milepaeler | Prosjektleder | Fremdriftsplan | Milepael |
| REQ-008 | Ikke-funksjonelt | Dokumentere analysen slik at den kan etterproves | Prosjektgruppen | Rapport og kode | Review |

Detaljert kravliste finnes i [requirements.json](requirements.json).

## Løsning

Losningen som skal utvikles er en tidsseriebasert analysepipeline der historiske manedlige salgstall for traktorer struktureres, deles i trenings- og testdata, analyseres og modelleres med en SARIMA-tilnaerming. Løsningen skal bestå av et dokumentert datagrunnlag, visualisering av trend og sesong, en begrunnet modellspesifikasjon, in-sample residualdiagnostikk, out-of-sample validering pa testsett, prognose for neste 12 maneder og tolkning av prognosene for produksjon og lager.

## Arbeidsnedbrytningsstruktur

Arbeidsnedbrytningsstrukturen utgjor den formelle omfangsbaselinen. Hovedstrukturen er:

1. Fase 1 - initiering
2. Fase 2 - planlegging
3. Fase 3 - gjennomforing
4. Fase 4 - avslutning

Viktige arbeidspakker i fase 3 er datainnsamling og forbehandling, modellvalg og estimering, modellvalidering, prognosearbeid og rapportutkast. Full WBS finnes i [wbs.json](wbs.json).

## Omfangsverifikasjon

Alle delleveranser skal verifiseres internt i gruppen før de brukes videre i prosjektet. Hver aktivitet skal derfor ha review som en egen avsluttende oppgave før aktiviteten kan lukkes formelt. Datagrunnlag skal kontrolleres før modellering. Modellvalg og tolkning skal gjennom en faglig gjennomlesning. Residualdiagnostikk skal dokumenteres i analysekapitlet, mens testsettresultater og feilmål skal presenteres i resultatkapitlet uten å gjenta metodeforklaringen. Den samlede vurderingen av modellens egnethet skal løftes til diskusjonskapitlet. Rapportutkast skal gjennom intern kvalitetssikring før peer review. Peer review brukes som ekstern faglig verifikasjon før sluttrevisjon.

## Fremdrift

Fremdriftsbaselinen følger kursfasene:

- Fase 1: 2026-01-12 til 2026-01-21
- Fase 2: 2026-02-11 til 2026-02-13
- Fase 3: starter 2026-03-09 med samlinger 2026-03-09, 2026-03-11, 2026-04-27 og 2026-04-29
- Fase 4: avslutning etter fase 3, styrt mot intern maldato 2026-05-15

Detaljert fremdriftsplan finnes i [schedule.json](schedule.json).

## Avhengighetsdiagram

`Caseforstaelse -> Proposal -> Planbaseline -> Datarensing -> Modellvalg -> Modellvalidering -> Prognose -> Rapportutkast -> Peer review -> Sluttleveranse`

## Gantt-plan

| Aktivitet | Start | Slutt |
| --- | --- | --- |
| Analysere case og databehov | 2026-01-12 | 2026-01-16 |
| Utarbeide proposal | 2026-01-16 | 2026-01-21 |
| Etablere planbaseline | 2026-02-11 | 2026-02-13 |
| Rense og strukturere data | 2026-03-09 | 2026-03-11 |
| Velge og estimere modell | 2026-03-11 | 2026-03-20 |
| Validere modell | 2026-03-20 | 2026-03-25 |
| Lage prognose og anbefalinger | 2026-03-25 | 2026-04-10 |
| Skrive rapportutkast | 2026-04-10 | 2026-04-27 |
| Peer review og revisjon | 2026-04-27 | 2026-04-29 |
| Ferdigstille rapport og presentasjon | 2026-04-30 | 2026-05-15 |

## Kritisk linje

`Proposal -> Planbaseline -> Datarensing -> Modellvalg -> Modellvalidering -> Prognose -> Rapportutkast -> Peer review -> Sluttleveranse`

## Milepæler

| Milepael | Dato | Status |
| --- | --- | --- |
| Case og problemstilling avklart | 2026-01-12 | Oppnadd |
| Godkjent proposal | 2026-01-21 | Oppnadd |
| Godkjent plan | 2026-02-13 | Oppnadd |
| Forste analyseutkast | 2026-03-11 | Planlagt |
| Hovedutkast klart for review | 2026-04-27 | Planlagt |
| Peer review gjennomfort | 2026-04-29 | Planlagt |
| Endelig innlevering og presentasjon | 2026-05-15 | Planlagt |

## Budsjett

Prosjektet har ikke et eget finansielt budsjett. Baseline-budsjettet settes derfor til 0 NOK i direkte kontantkostnader. Ressursforbruket styres i stedet som studenttid og oppmerksomhet.

## Kostnadsfordeling per leveranse

Det er ingen direkte prosjektkostnader som fordeles per leveranse. Dersom gruppen onsker intern oppfolging, anbefales tidsbruk registrert per hovedleveranse:

- Proposal
- Plan
- Analyse og modellering
- Rapport og presentasjon

## Ressurskostnader

Det budsjetteres ikke med eksterne personalkostnader. Studentenes arbeidsinnsats er prosjektets viktigste ressursbidrag.

## Kostnadskurve

Prosjektet har ingen formell kostnadskurve i kroner. Dersom arbeidsinnsats visualiseres, vil den være lav i fase 1 og 2, stige markant i fase 3 og toppe seg mot slutten av fase 4.

## Risiko

Risikostyringen bygger pa et enkelt risikoregister med skala for sannsynlighet og konsekvens. De viktigste risikoene er databegrensninger, utilstrekkelig modelltilpasning, fremdriftsbrudd mellom samlinger, uklar rollefordeling og sent oppdagede endringsbehov etter peer review.

Topprisikoene per 2026-03-09 er:

1. Datagrunnlaget er ikke tilstrekkelig representativt.
2. SARIMA gir utilstrekkelig modelltilpasning.
3. Fremdriften sprekker mellom samlingene.

Fullt risikoregister finnes i [risk.json](risk.json).

## Prosess for risikostyring

Risikoregisteret skal gjennomgas i gruppen minst ukentlig i fase 3 og ved hver kurssamling. Risikoeiere har ansvar for a folge opp utlosere og iverksette avbotende tiltak tidlig. Nye risikoer legges fortlopende til dersom prosjektet endrer retning eller forutsetninger.

## Risikoregister

Risikoregisteret er etablert som en egen baselinefil med risiko-ID, kategori, eier, vurdert sannsynlighet, konsekvens og tiltaksplan. Gjeldende versjon finnes i [risk.json](risk.json).

## Saker

| Sak | Status | Ansvarlig | Frist |
| --- | --- | --- | --- |
| Fylle inn endelige gruppemedlemmer i proposal og plan | Apen | Prosjektleder | 2026-03-11 |
| Avklare intern rollefordeling i gruppen | Apen | Prosjektgruppen | 2026-03-09 |
| Avklare om intern maldato 2026-05-15 samsvarer med fagets faktiske innlevering | Apen | Prosjektleder | 2026-04-27 |

## Interessenter

| Interessent | Rolle | Innflytelse | Interesse |
| --- | --- | --- | --- |
| Emneansvarlig LOG650 | Sponsor og godkjenner | Hoy | Hoy |
| Prosjektgruppen | Utforende team | Hoy | Hoy |
| Faglaerer og medstudenter | Review og faglig tilbakemelding | Middels | Hoy |
| PowerHorse | Simulert kunde | Lav | Middels |

## Ressurser

### Prosjektteam

Prosjektteamet bestar av studentgruppen. Det anbefales at gruppen formaliserer minst disse rollene:

- Prosjektleder
- Dataansvarlig
- Analyseansvarlig
- Redaksjonsansvarlig

### Ressursbelastning

Ressursbelastningen er forventet a vaere lav i fase 1 og 2, middels i starten av fase 3 og hoy i perioden 2026-03-20 til 2026-05-15, nar analyse, rapportskriving og revisjon overlapper.

### Kritiske ressurser

- Tilgang til case og data
- Analysekompetanse i gruppen
- Tid til samkjort skriving og revisjon
- Peer review innen planlagt tidsvindu

## Kommunikasjon

### Ukentlige saksstatusmoter

Gruppen gjennomforer ett kort statusmote per uke i fase 3 og 4. Motet skal dekke fremdrift siden sist, neste arbeidsoppgaver, apne saker og risikoer som har endret seg.

### Manedlige prosjektgjennomganger

Kurssamlingene fungerer som formelle prosjektgjennomganger. Der rapporteres status pa milepaeler, sentrale funn og eventuelle behov for korrigering.

### Moter i endringskontrollstyret

Ved behov fungerer prosjektgruppen sammen med faglaerer eller emneansvarlig som et enkelt endringskontrollforum for a vurdere større endringer i omfang eller fremdrift.

### Annen kommunikasjon

Lopende kommunikasjon skjer i gruppens Teams-kanal og gjennom commits eller filer i GitHub-repositoriet.

## Kvalitet

Kvalitetsstyringen bygger pa fire prinsipper:

- kvalitet ma bygges inn i arbeidet underveis
- analyse, tekst og figurer ma vaere konsistente
- alle viktige leveranser skal gjennomleses av minst en annen i gruppen
- resultatene ma vaere egnet for formalet, ikke bare teknisk korrekte

For rapportstrukturen gjelder folgende arbeidsdeling:

- Kapittel 7 brukes til analyse, valideringsfunn og tekniske vurderinger.
- Kapittel 8 brukes til komprimerte sluttresultater og nokkeltall.
- Kapittel 9 brukes til faglig vurdering av modellens egnethet, begrensninger og praktiske implikasjoner.

### Fagfellevurderinger

Alle viktige leveranser skal ha minst en intern fagfellevurdering før de anses som ferdige.

### Uformelle fagfellevurderinger

Proposal, prosjektplan, analyseutkast og presentasjon skal gjennom uformell review i gruppen. Eier av leveransen samler kommentarer og oppdaterer dokumentet.

### Formelle fagfellevurderinger

Det planlegges ingen egne formelle QA-reviews med ekstern organisasjon. Peer review i emnet fungerer likevel som en mer formalisert faglig gjennomgang mot slutten av fase 3.

### Brukerreviews

Brukerreview tolkes i dette prosjektet som review fra faglaerer, medstudenter og caseperspektivet. Malet er a bekrefte at losningen gir mening for en virksomhet som skal planlegge produksjon og lager.

## Anskaffelser

Prosjektet krever ingen egne anskaffelser. Eksisterende verktoy, kursmateriell og repositorium brukes som grunnlag.

## Endringskontrollprosess

1. Endringen beskrives kort med arsaken til at den er nodvendig.
2. Prosjektgruppen vurderer konsekvenser for krav, milepaeler, arbeidsmengde og risiko.
3. Dersom endringen pavirker en godkjent faseleveranse eller setter en milepael i fare, tas den opp med faglaerer eller emneansvarlig.
4. Godkjente endringer oppdateres i planfilene og kommuniseres til hele gruppen.
