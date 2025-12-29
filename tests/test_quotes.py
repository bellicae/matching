import unittest
from pathlib import Path
import shutil
from src.models.quote_request import QuoteRequest
from src.models.quote_response import QuoteResponse
from src.services.quote_service import QuoteService


class TestQuoteService(unittest.TestCase):

    def setUp(self):
        # Create a temporary data directory for testing
        self.test_data_dir = Path("tests/test_data")
        quotes_dir = self.test_data_dir / "quotes"
        quotes_dir.mkdir(parents=True, exist_ok=True)

        # Initialize empty JSON files
        (quotes_dir / "quote_requests.json").write_text('{"quote_requests": []}', encoding="utf-8")
        (quotes_dir / "quote_responses.json").write_text('{"quote_responses": []}', encoding="utf-8")

        # Initialize the service
        self.quote_service = QuoteService(str(self.test_data_dir))

    def tearDown(self):
        # Remove the temporary data directory after tests
        if self.test_data_dir.exists():
            shutil.rmtree(self.test_data_dir)

    def test_add_and_get_quote_request(self):
        request = QuoteRequest(
            request_id="qr001",
            player_id="p001",
            host_id="h001",
            character_name= "Wizard"
            )
