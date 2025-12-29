import json
from pathlib import Path
from typing import Dict, Optional


class Host:
    def __init__(
        self,
        host_id: str,
        name: str,
        race: str,
        base_rate: float,
        services: Optional[Dict[str, float]] = None,
        costumes_owned: Optional[Dict[str, float]] = None,
        accepts_custom_costumes: bool = True,
        custom_costume_base_fee: float = 0.0
    ):
        self.host_id = host_id
        self.name = name
        self.race = race
        self.base_rate = base_rate
        self.services = services if services else {}
        self.costumes_owned = costumes_owned if costumes_owned else {}
        self.accepts_custom_costumes = accepts_custom_costumes
        self.custom_costume_base_fee = custom_costume_base_fee

    @classmethod
    def from_dict(cls, data: dict):
        """
        Create a Host object from a dictionary (e.g., loaded from JSON)
        """
        return cls(
            host_id=data.get("host_id"),
            name=data.get("name"),
            race=data.get("race"),
            base_rate=data.get("base_rate", 0),
            services=data.get("services", {}),
            costumes_owned=data.get("costumes_owned", {}),
            accepts_custom_costumes=data.get("accepts_custom_costumes", True),
            custom_costume_base_fee=data.get("custom_costume_base_fee", 0)
        )

    def to_dict(self) -> dict:
        """
        Convert the Host object back to a dictionary for JSON serialization
        """
        return {
            "host_id": self.host_id,
            "name": self.name,
            "race": self.race,
            "base_rate": self.base_rate,
            "services": self.services,
            "costumes_owned": self.costumes_owned,
            "accepts_custom_costumes": self.accepts_custom_costumes,
            "custom_costume_base_fee": self.custom_costume_base_fee
        }

    def has_services(self, services_name: str, included_only: bool = False) -> bool:
        """
        Check if host offers a theme. 
        If included_only is True, only services with 0 extra cost count.
        """
        if services_name not in self.services:
            return False
        if included_only and self.services[services_name] > 0:
            return False
        return True

    def owns_costume(self, character_name: str) -> bool:
        """
        Check if host owns a specific costume
        """
        return character_name in self.costumes_owned

    def costume_extra_cost(self, character_name: str) -> Optional[float]:
        """
        Return the extra cost for a costume, or None if not owned
        """
        return self.costumes_owned.get(character_name)

    def can_fulfill_custom_costume(self) -> bool:
        """
        Check if host accepts custom costume requests
        """
        return self.accepts_custom_costumes


def load_hosts_from_file(file_path: str) -> list:
    """
    Load all hosts from a JSON file and return a list of Host objects
    """
    path = Path(file_path)
    if not path.is_file():
        raise FileNotFoundError(f"Hosts file not found: {file_path}")

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    hosts_list = data.get("hosts", [])
    return [Host.from_dict(host_data) for host_data in hosts_list]


# Example usage:
# hosts = load_hosts_from_file("data/hosts.json")
# print(hosts[0].name, hosts[0].base_rate)
