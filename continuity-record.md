# Continuity Record

## Project

Vendor Verifier

## Assessment

UBI – The Root Access Network – GRC Analyst Stage 6

## Objective

Verify vendor evidence, compare technical evidence with vendor claims, identify contradictions, produce governance recommendations, and generate required assessment artifacts.

## Environment

- Ubuntu Linux
- Python 3.14
- Virtual environment (.venv)
- Nano editor
- Git
- GitHub

## Reproduction Steps

1. Create and activate the Python virtual environment.
2. Install project dependencies.
3. Place the supplied evidence JSON files in the `input/` directory.
4. Run:

```bash
python main.py
```

5. Generate the PDF report:

```bash
python generate_pdf.py
```

6. Review all generated files in the `output/` directory.

## Repository

Git history documents the incremental implementation of the assessment pipeline.

## Notes

No raw evidence files were modified during the assessment. Generated artifacts are derived from the supplied evidence package.
