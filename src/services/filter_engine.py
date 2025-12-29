from typing import List
from src.models.host import Host
from src.models.player_filter import PlayerFilter


class FilterEngine:
    """
    Engine to filter hosts based on player preferences
    """

    @staticmethod
    def filter_hosts(hosts: List[Host], player_filter: PlayerFilter) -> List[Host]:
        """
        Return a list of hosts matching the player filter
        """
        matching_hosts = [host for host in hosts if player_filter.matches_host(host)]
        return matching_hosts


# Example usage:
# from services.data_loader import DataLoader
# from models.player_filter import PlayerFilter
#
# loader = DataLoader("data")
# hosts = loader.load_hosts()
#
# player_filter = PlayerFilter(
#     races=["Ranger", "Warrior"],
#     required_themes=["fantasy", "forest"],
#     require_included_themes=True,
#     max_rate=200,
#     required_costume="Elf Warrior",
#     allow_custom_costume=True,
#     max_custom_costume_price=60
# )
#
# matches = FilterEngine.filter_hosts(hosts, player_filter)
# for host in matches:
#     print(f"{host.name} ({host.race}) - ${host.base_rate}/hr")
