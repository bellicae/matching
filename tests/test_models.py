import unittest
from src.models.host import Host
from src.models.quote_request import QuoteRequest
from src.models.quote_response import QuoteResponse


class TestModels(unittest.TestCase):

    def test_host_creation_and_dict(self):
        host_data = {
            "host_id": "h001",
            "name": "Aria",
            "race": "Ranger",
            "base_rate": 150,
            "services": {"fantasy": 0, "forest": 20},
            "costumes_owned": {"Elf Warrior": 30},
            "accepts_custom_costumes": True,
            "custom_costume_base_fee": 50
        }

        host = Host.from_dict(host_data)
        self.assertEqual(host.host_id, "h001")
        self.assertEqual(host.name, "Aria")
        self.assertEqual(host.race, "Ranger")
        self.assertEqual(host.base_rate, 150)
        self.assertTrue(host.has_services("fantasy"))
        self.assertFalse(host.has_services("medieval"))
        self.assertTrue(host.owns_costume("Elf Warrior"))
        self.assertEqual(host.costume_extra_cost("Elf Warrior"), 30)
        self.assertTrue(host.can_fulfill_custom_costume())

        # Test to_dict
        dict_out = host.to_dict()
        self.assertEqual(dict_out["host_id"], "h001")
        self.assertEqual(dict_out["race"], "Ranger")

    def test_quote_request_creation_and_dict(self):
        request_data = {
            "request_id": "qr001",
            "player_id": "p001",
            "host_id": "h001",
            "character_name": "Dragon Knight",
            "details": "Need full armor and props"
        }

        request = QuoteRequest.from_dict(request_data)
        self.assertEqual(request.request_id, "qr001")
        self.assertEqual(request.player_id, "p001")
        self.assertEqual(request.host_id, "h001")
        self.assertEqual(request.character_name, "Dragon Knight")
        self.assertEqual(request.details, "Need full armor and props")

        # Test to_dict
        dict_out = request.to_dict()
