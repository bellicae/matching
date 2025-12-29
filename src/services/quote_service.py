import json
from pathlib import Path
from typing import List, Optional
from src.models.quote_request import QuoteRequest, load_quote_requests
from src.models.quote_response import QuoteResponse, load_quote_responses


class QuoteService:
    """
    Service to handle quote requests and responses for custom costumes
    """

    def __init__(self, data_dir: str):
        self.data_dir = Path(data_dir)
        self.requests_file = self.data_dir / "quotes" / "quote_requests.json"
        self.responses_file = self.data_dir / "quotes" / "quote_responses.json"

        self.requests: List[QuoteRequest] = load_quote_requests(str(self.requests_file))
        self.responses: List[QuoteResponse] = load_quote_responses(str(self.responses_file))

    def add_quote_request(self, request: QuoteRequest):
        """
        Add a new quote request
        """
        self.requests.append(request)
        self._save_requests()

    def add_quote_response(self, response: QuoteResponse):
        """
        Add a host's response to a quote request
        """
        self.responses.append(response)
        self._save_responses()

    def get_responses_for_request(self, request_id: str) -> List[QuoteResponse]:
        """
        Return all responses for a specific quote request
        """
        return [r for r in self.responses if r.request_id == request_id]

    def _save_requests(self):
        """
        Save all quote requests back to JSON file
        """
        self.requests_file.parent.mkdir(parents=True, exist_ok=True)
        with open(self.requests_file, "w", encoding="utf-8") as f:
            data = {"quote_requests": [r.to_dict() for r in self.requests]}
            json.dump(data, f, indent=4)

    def _save_responses(self):
        """
        Save all quote responses back to JSON file
        """
        self.responses_file.parent.mkdir(parents=True, exist_ok=True)
        with open(self.responses_file, "w", encoding="utf-8") as f:
            data = {"quote_responses": [r.to_dict() for r in self.responses]}
            json.dump(data, f, indent=4)

    def find_request_by_player_and_host(self, player_id: str, host_id: str) -> Optional[QuoteRequest]:
        """
        Find a quote request for a given player and host
        """
        for req in self.requests:
            if req.player_id == player_id and req.host_id == host_id:
                return req
        return None


# Example usage:
# from models.quote_request import QuoteRequest
# from models.quote_response import QuoteResponse
#
# service = QuoteService("data")
#
# # Create a new quote request
# new_request = QuoteRequest(
#     request_id="qr003",
#     player_id="p001",
#     host_id="h001",
#     character_name="Dragon Knight",
#     details="Need full armor, ready in 2 weeks"
# )
# service.add_quote_request(new_request)
#
# # Host responds to quote
# response = QuoteResponse(
#     r
