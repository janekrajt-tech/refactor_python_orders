## Kodgranskning av order_report.py



## 1

### Observation
Statusmeddelanden skrivs ut direkt med print()
### Konsekvens
Det blir svårare att styra och strukturera loggningen, exempelvis skilja mellan information, varningar och fel.
### Förslag 
Använd Python-modulen logging och olika loggnivåer, exempelvis INFO, WARNING och ERROR.

## 2

### Observation
All funktionalitet, inklusive datainläsning, datarensning, beräkningar och skapande av rapporter, ligger i samma fil och körs direkt.
### Konsekvens
Delarna blir svårare att testa, återanvända och underhålla individuellt.
### Förslag 
Dela upp funktionaliteten i mindre funktioner och vid behov separata moduler med tydliga ansvarsområden.

## 3

### Observation 
Det finns inga automatiserade tester för funktionerna eller beräkningarna.
### Konsekvens
Det blir svårt att upptäcka om förändringar i koden leder till felaktiga resultat, exempelvis vid datarensning eller beräkning av försäljning och returgrad.
### Förslag 
Lägg till automatiserade tester, exempelvis med pytest, för centrala delar som datarensning, beräkning av ordervärde och returgrad.

## 4

### Observation
Generella felmeddelanden
### Konsekvens
Det blir svårt att snabbt identifiera vilken del av programmet som orsakat felet och vad som faktiskt är fel.
### Förslag 
Använd mer specifika undantag och tydligare felmeddelanden, exempelvis separata hanteringar för problem med filinläsning, saknade kolumner och felaktiga datatyper.

## 5

### Observation
Saknade värdena ersätts med 1
### Konsekvens
Det innebär ett antagande om att en order med saknat eller ogiltigt antal faktiskt hade quantity = 1. Det kan ge felaktiga försäljningsvärden och därmed påverka rapportens resultat.
### Förslag 
ndersök varför värden saknas och välj en metod utifrån datans betydelse. Exempelvis kan rader med saknad quantity flaggas eller hanteras separat istället för att automatiskt anta värdet 1.

## 6

### Observation
output-mappen skapas inte automatiskt
### Konsekvens
Om output-mappen saknas kommer programmet att misslyckas när resultatet ska sparas.
### Förslag 
Skapa mappen automatiskt innan resultatfilerna sparas, exempelvis med os.makedirs()
## 7

### Observation
Liknande logik för att skapa försäljningsrapporter upprepas i result1 och result2.
### Konsekvens
Duplicering gör koden längre och innebär att ändringar behöver göras på flera ställen, vilket ökar risken för inkonsekvenser.
### Förslag 
Skapa en funktion som kan återanvändas för att generera rapporter baserat på olika grupperingskolumner.

## 8

### Observation
Programmet utför datainläsning och skriver filer direkt när skriptet körs.
### Konsekvens
Det gör funktionaliteten svårare att återanvända och testa eftersom import eller körning av filen kan orsaka sidoeffekter.
### Förslag
Flytta körlogiken till funktioner och använnd if och main 
