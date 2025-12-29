from pathlib import Path
from typing import List
from models.host import Host, load_hosts_from_file
from models.quote_request import QuoteRequest, load_quote_requests
from models.quote_response import QuoteResponse, load_quote_responses


class DataLoader:
    """
    Centralized loader for all JSON data files
    """

    def __init__(self, data_dir: str):
        self.data_dir = Path(data_dir)
        if not self.data_dir.is_dir():
            raise FileNotFoundError(f"Data directory not found: {data_dir}")

    def load_hosts(self) -> List[Host]:
        hosts_file = self.data_dir / "hosts.json"
        return load_hosts_from_file(str(hosts_file))

    def load_quote_requests(self) -> List[QuoteRequest]:
        requests_file = self.data_dir / "quotes" / "quote_requests.json"
        return load_quote_requests(str(requests_file))

    def load_quote_responses(self) -> List[QuoteResponse]:
        responses_file = self.data_dir / "quotes" / "quote_responses.json"
        return load_quote_responses(str(responses_file))


# Example usage:
# loader = DataLoader("data")
# hosts = loader.load_hosts()
# requests = loader.load_quote_requests()
# responses = loader.load_quote_responses()
#
# print(f"{len(hosts)} hosts loaded.")
# print(f"{len(requests)} quote requests loaded.")
# print(f"{len(responses)} quote responses loaded.")
