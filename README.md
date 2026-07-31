# Vendor Verifier

## Overview

Vendor Verifier is a Python-based evidence verification and vendor risk assessment tool developed for the **UBI – The Root Access Network GRC Analyst Stage 6** assessment.

The application validates machine-readable vendor evidence, compares vendor claims with technical evidence, detects contradictions, and generates governance artifacts that support vendor risk decisions.

---

## Features

- Typed JSON ingestion
- JSON Schema validation
- TLS version verification
- Privileged MFA verification
- Duplicate privileged event detection
- Audit hash-chain verification
- Contradiction matrix generation
- Evidence verdict generation
- Vendor risk register generation
- Data flow graph generation
- Contract redline recommendations
- Monitoring plan generation
- Vendor risk memo (PDF)

---

## Project Structure

```
vendor-verifier/
├── fixtures/
├── input/
├── output/
├── schemas/
├── tests/
├── validator/
├── main.py
├── Makefile
├── requirements.txt
└── README.md
```

---

## Requirements

- Python 3.14+
- pip
- Virtual environment (recommended)

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run the validator

```bash
make run
```

or

```bash
python main.py
```

---

## Run the test suite

```bash
make test
```

or

```bash
pytest -v
```

---

## Generate the PDF report

```bash
python generate_pdf.py
```

The report is saved to:

```
output/vendor-risk-memo.pdf
```

---

## Generated Outputs

Running the validator produces:

- evidence-verdicts.json
- contradiction-matrix.csv
- vendor-risk-register.csv
- contract-redlines.md
- monitoring-plan.yaml
- data-flow.graphml
- evidence-index.csv
- integrity-attestation.md
- vendor-risk-memo.pdf

---

## Technologies

- Python
- Pytest
- JSON Schema
- ReportLab
- NetworkX
- Git
- GitHub
- Ubuntu Linux

---

## Author

**Orji Ogechukwu Confidence
