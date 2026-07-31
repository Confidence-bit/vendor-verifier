# Vendor Verifier

## Overview

Vendor Verifier is a Python-based governance, risk, and compliance (GRC) assessment tool developed for the UBI – The Root Access Network Advanced Programme (Stage 6).

The project validates machine-readable vendor evidence, compares technical evidence against vendor claims, identifies contradictions, and generates assessment artifacts to support vendor risk decisions.

---

## Features

- Validates vendor JSON evidence
- Checks TLS configuration compliance
- Detects privileged access without MFA
- Detects duplicate privileged access events
- Verifies audit log hash chain integrity
- Generates machine-readable evidence verdicts
- Produces a contradiction matrix
- Generates a vendor risk register
- Produces a data flow graph
- Generates a vendor risk assessment memo (PDF)
- Creates supporting governance documentation

---

## Project Structure

```
vendor-verifier/
├── input/
├── output/
├── schemas/
├── tests/
├── validator/
├── main.py
├── generate_pdf.py
├── requirements.txt
└── README.md
```

---

## Requirements

- Python 3.14
- Virtual Environment (recommended)

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Assessment

Execute:

```bash
python main.py
```

This validates the supplied evidence and generates assessment artifacts in the `output/` directory.

---

## Generate the PDF Report

Run:

```bash
python generate_pdf.py
```

The report will be generated as:

```
output/vendor-risk-memo.pdf
```

---

## Generated Deliverables

The project produces:

- evidence-verdicts.json
- contradiction-matrix.csv
- vendor-risk-register.csv
- contract-redlines.md
- monitoring-plan.yaml
- evidence-index.csv
- data-flow.graphml
- vendor-risk-memo.pdf
- integrity-attestation.md

---

## Technologies Used

- Python 3.14
- JSON
- ReportLab
- Git
- GitHub
- Ubuntu Linux

---

## Author

Orji Ogechukwu Confidence
