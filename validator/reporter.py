import json
import os


def write_verdicts(verdicts, filename="output/evidence-verdicts.json"):
    """
    Write all validation verdicts to a JSON file.
    """

    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(verdicts, file, indent=4)

    print(f"\n✅ Evidence verdicts written to {filename}")
