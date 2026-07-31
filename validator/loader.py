import json
from pathlib import Path


def load_json(filepath: str) -> dict:
    """
    Load a JSON file and return its contents.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the JSON is invalid.
    """
    path = Path(filepath)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {filepath}")

    try:
        with path.open("r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON in {filepath}: {e}")
