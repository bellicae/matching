import unittest
from src.models.host import Host
from src.models.player_filter import PlayerFilter
from src.services.filter_engine import FilterEngine


class TestFilterEngine(unittest.TestCase):

    def setUp(self):
        # Create sample hosts
        self.hosts = [
            Host(
                host_id="h001",
                name="Aria",
                race="Ranger",
                base_rate=150,
                services={"fantasy": 0, "forest": 20},
                costumes_owned={"Elf Warrior": 30},
                accepts_custom_costumes=True,
                custom_costume_base_fee=50
            ),
            Host(
                host_id="h002",
                name="Gorak",
                race="Warrior",
                base_rate=120,
                services={"medieval": 0, "dungeon": 15},
                costumes_owned={"Knight": 0},
                accepts_custom_costumes=False,
                custom_costume_base_fee=0
            ),
            Host(
                host_id="h003",
                name="Lina",
                race="Mage",
                base_rate=200,
                services={"fantasy": 0, "forest": 0},
                costumes_owned={"Wizard": 40},
                accepts_custom_costumes=True,
                custom_costume_base_fee=70
            )
        ]

    def test_filter_by_race(self):
        player_filter = PlayerFilter(race=["Ranger"])
        result = FilterEngine.filter_hosts(self.hosts, player_filter)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].race, "Ranger")

    def test_filter_by_theme_included_only(self):
        player_filter = PlayerFilter(
            required_services=["fantasy"],
            require_included_services=True
        )
        result = FilterEngine.filter_hosts(self.hosts, player_filter)
        self.assertEqual(len(result), 2)  # Aria (50) and Lina (70)

    def test_filter_by_max_rate(self):
        player_filter = PlayerFilter(max_rate=150)
        result = FilterEngine.filter_hosts(self.hosts, player_filter)
        self.assertEqual(len(result), 2)  # Aria (150) and Gorak (120)

    def test_filter_by_required_costume(self):
        player_filter = PlayerFilter(
            required_costume="Elf Warrior",
            allow_custom_costume=False
        )
        result = FilterEngine.filter_hosts(self.hosts, player_filter)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].name, "Aria")

    def test_filter_allow_custom_costume(self):
        player_filter = PlayerFilter(
            required_costume="Dragon Knight",
            allow_custom_costume=True,
            max_custom_costume_price=60
        )
        result = FilterEngine.filter_hosts(self.hosts, player_filter)
        self.assertEqual(len(result), 1)  # Aria (50), Lina (70 excluded because max 60)
        self.assertEqual(result[0].name, "Aria")


if __name__ == "__main__":
    unittest.main()
