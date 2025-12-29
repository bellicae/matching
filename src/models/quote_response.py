import json
from pathlib import Path
from typing import List, Optional, Dict


class QuoteResponse:
    def __init__(
        self,
        request_id: str,
        quoted_price: float,
        estimated_time_days: int,
        notes: Optional[str] = ""
    ):
        self.request_id = request_id
        self.quoted_price = quoted_price
        self.estimated_time_days = estimated_time_days
        self.notes = notes

    @classmethod
    def from_dict(cls, data: Dict):
        """
        Create a QuoteResponse object from a dictionary (e.g., loaded from JSON)
        """
        return cls(
            request_id=data.get("request_id"),
            quoted_price=data.get("quoted_price", 0.0),
            estimated_time_days=data.get("estimated_time_days", 0),
            notes=data.get("notes", "")
        )

    def to_dict(self) -> Dict:
        """
        Convert the QuoteResponse object back to a dictionary for JSON serialization
        """
        return {
            "request_id": self.request_id,
            "quoted_price": self.quoted_price,
            "estimated_time_days": self.estimated_time_days,
            "notes": self.notes
        }


def load_quote_responses(file_path: str) -> List[QuoteResponse]:
    """
    Load all quote responses from a JSON file and return a list of QuoteResponse objects
    """
    path = Path(file_path)
    if not path.is_file():
        raise FileNotFoundError(f"Quote responses file not found: {file_path}")

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    responses_list = data.get("quote_responses", [])
    return [QuoteResponse.from_dict(resp) for resp in responses_list]


# Example usage:
# responses = load_quote_responses("data/quotes/quote_responses.json")
# for r in responses:
#     print(r.request_id, r.quoted_price, r.estimated_time_days)
