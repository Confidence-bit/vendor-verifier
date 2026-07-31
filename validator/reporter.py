import csv
import json
import os


def write_verdicts(verdicts, filename="output/evidence-verdicts.json"):
    """
    Write all validation findings to a JSON file.
    """

    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(verdicts, file, indent=4)

    print(f"\n✅ Wrote {len(verdicts)} verdict(s) to {filename}")


def write_contradiction_matrix(
    rows,
    filename="output/contradiction-matrix.csv"
):
    """
    Write the contradiction matrix to a CSV file.
    """

    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, "w", newline="", encoding="utf-8") as file:

        writer = csv.DictWriter(
            file,
            fieldnames=[
                "claim_id",
                "control",
                "vendor_claim",
                "evidence",
                "verdict",
                "reason",
            ],
        )

        writer.writeheader()

        for row in rows:
            writer.writerow(row)

    print(f"✅ Wrote contradiction matrix to {filename}")
