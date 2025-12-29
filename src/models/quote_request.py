import json
from pathlib import Path
from typing import List, Optional, Dict


class QuoteRequest:
    def __init__(
        self,
        request_id: str,
        player_id: str,
        host_id: str,
        character_name: str,
        details: Optional[str] = ""
    ):
        self.request_id = request_id
        self.player_id = player_id
        self.host_id = host_id
        self.character_name = character_name
        self.details = details

    @classmethod
    def from_dict(cls, data: Dict):
        """
        Create a QuoteRequest object from a dictionary (e.g., loaded from JSON)
        """
        return cls(
            request_id=data.get("request_id"),
            player_id=data.get("player_id"),
            host_id=data.get("host_id"),
            character_name=data.get("character_name"),
            details=data.get("details", "")
        )

    def to_dict(self) -> Dict:
        """
        Convert the QuoteRequest object back to a dictionary for JSON serialization
        """
        return {
            "request_id": self.request_id,
            "player_id": self.player_id,
            "host_id": self.host_id,
            "character_name": self.character_name,
            "details": self.details
        }


def load_quote_requests(file_path: str) -> List[QuoteRequest]:
    """
    Load all quote requests from a JSON file and return a list of QuoteRequest objects
    """
    path = Path(file_path)
    if not path.is_file():
        raise FileNotFoundError(f"Quote requests file not found: {file_path}")

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    requests_list = data.get("quote_requests", [])
    return [QuoteRequest.from_dict(req) for req in requests_list]


# Example usage:
# requests = load_quote_requests("data/quotes/quote_requests.json")
# for r in requests:
#     print(r.request_id, r.character_name)
