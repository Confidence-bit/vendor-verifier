from dataclasses import dataclass
from typing import Optional


@dataclass
class Verdict:
    """
    Represents the result of a single verification check.
    """

    check_id: str
    status: str
    code: str
    severity: str
    message: str

    locator: Optional[str] = None
    claim_id: Optional[str] = None
