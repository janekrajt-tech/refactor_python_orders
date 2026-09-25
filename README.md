# Refactor Python Orders

## Vad projektet gör

Projektet läser in orderdata från en CSV-fil och skapar rapporter över försäljning och returer. Programmet kontrollerar data, utför beräkningar och sparar resultatet som CSV-filer.

## Installation

1. Skapa en virtuell miljö:

python -m venv venv

2. Aktivera miljön i Git Bash:

source venv/Scripts/activate

3. Installera beroenden:

pip install -r requirements.txt

## Beroenden

Projektet använder Python, pandas och pytest. Alla beroenden finns i requirements.txt.

## Köra programmet

Kör programmet från projektets rotmapp:

python src/main.py

De refaktorerade rapporterna sparas i mappen output_new medans rapporterna från den original filen i output.

## Köra tester

Kör de automatiska testerna med:

python -m pytest

Testerna kontrollerar bland annat validering av obligatoriska kolumner samt beräkning av ordervärden och rabatter.

## Projektstruktur

refactor_python_orders/
├── data/
│   └── orders.csv
├── output/
├── output_new
├── src/
│   ├── config.py
│   ├── load.py
│   ├── main.py
│   ├── order_report.py
│   ├── report.py
│   ├── save.py
│   ├── transform.py
│   └── validate.py
├── tests/
│   ├── test_transform.py
│   └── test_validate.py
├── .gitignore
├── code_review.md
├── README.md
├── reflection.md
└── requirements.txt