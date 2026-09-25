# Reflektion

## Vilka var de viktigaste problemen i originalkoden?
- All kod låg i samma fil → svårt att testa och underhålla.

- print() användes för status → ersattes med logging.

- Inga automatiserade tester → pytest lades till.

- Generell felhantering → tydligare ValueError och felmeddelanden.

- Programmet körde allt direkt → körlogiken flyttades till run_report() och if __name__ == "__main__".

## Vilka förändringar tycker du förbättrade programmet mest?
Jag tycker att uppdelningen i flera moduler och införandet av automatiserade tester förbättrade programmet mest. Koden blev lättare att förstå, testa och underhålla. Logging gjorde också programmets körning tydligare.

## Varför valde du den projektstruktur du använde?
Jag valde att dela upp programmet efter ansvar. Exempelvis hanterar load.py inläsning, validate.py validering, transform.py datatransformering, report.py rapporter och save.py sparande. Det gör varje del mer fokuserad och enklare att testa och ändra.

## Var använde du OOP/dataclass och varför passade det där?
Jag använde OOP i config.py genom en dataclass (ReportConfig) för att samla programmets konfiguration, till exempel sökvägen till indata och output-mappen. Det passade bra eftersom relaterade inställningar hålls samlade på ett tydligt och enkelt sätt.

## Vilka viktiga beteenden skyddar dina automatiska tester, och vilken nytta ger testerna om programmet förändras i framtiden?
Testerna skyddar bland annat att obligatoriska kolumner valideras korrekt och att ordervärde och rabatter beräknas rätt. De kontrollerar även att ett förväntat fel uppstår när en kolumn saknas.
Om programmet ändras i framtiden kan testerna snabbt upptäcka om någon ändring har gjort att den befintliga funktionaliteten eller beräkningarna slutat fungera.

## Vad var svårast?
I början var det svårast att förstå var man ska börja ifrån och identifiera felen och hitta rätt lösning.

## Vad hade du velat förbättra ytterligare om du haft mer tid?
Jag hade velat lägga till fler automatiska tester, framför allt för tom data, ogiltiga värden och rapporterna per kategori och region. Jag hade även velat förbättra hanteringen av saknade värden, exempelvis quantity, så att programmet inte automatiskt antar att värdet är 1.