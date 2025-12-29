from typing import List, Dict, Optional
from src.models.host import Host  # Make sure your imports match your folder structure


class PlayerFilter:
    def __init__(
        self,
        race: Optional[List[str]] = None,           # List of race to include (None = all)
        required_services: Optional[List[str]] = None,  # services the host must have
        require_included_services: bool = False,        # True = theme must be included, not extra
        max_theme_extra_cost: Optional[Dict[str, float]] = None,  # Optional max extra per theme
        min_rate: Optional[float] = None,             # Minimum base rate
        max_rate: Optional[float] = None,             # Maximum base rate
        required_costume: Optional[str] = None,       # Costume player wants
        max_costume_extra_cost: Optional[float] = None, # Max extra for costume
        allow_custom_costume: bool = False,           # Accept hosts that can do custom costume
        max_custom_costume_price: Optional[float] = None # Max fee for custom costume
    ):
        self.race = race
        self.required_services = required_services or []
        self.require_included_services = require_included_services
        self.max_theme_extra_cost = max_theme_extra_cost or {}
        self.min_rate = min_rate
        self.max_rate = max_rate
        self.required_costume = required_costume
        self.max_costume_extra_cost = max_costume_extra_cost
        self.allow_custom_costume = allow_custom_costume
        self.max_custom_costume_price = max_custom_costume_price

    def matches_host(self, host: Host) -> bool:
        """
        Return True if the host satisfies all filter conditions
        """
        # Check class
        if self.race and host.race not in self.race:
            return False

        # Check services
        for services in self.required_services:
            if not host.has_services(services, included_only=self.require_included_services):
                return False

        # Check base rate
        if self.min_rate is not None and host.base_rate < self.min_rate:
            return False
        if self.max_rate is not None and host.base_rate > self.max_rate:
            return False

        # Check costume
        if self.required_costume:
            if host.owns_costume(self.required_costume):
                extra = host.costume_extra_cost(self.required_costume) or 0
                if self.max_costume_extra_cost is not None and extra > self.max_costume_extra_cost:
                    return False
            elif self.allow_custom_costume:
                if not host.can_fulfill_custom_costume():
                    return False
                if self.max_custom_costume_price is not None and host.custom_costume_base_fee > self.max_custom_costume_price:
                    return False
            else:
                return False  # Host does not have the costume and custom costume not allowed

        return True


# Example usage:
# from models.host import load_hosts_from_file
# hosts = load_hosts_from_file("data/hosts.json")
# filter1 = PlayerFilter(
#     race=["Ranger", "Mage"],
#     required_services=["fantasy", "forest"],
#     require_included_services=True,
#     max_rate=200,
#     required_costume="Elf Warrior",
#     allow_custom_costume=True,
#     max_custom_costume_price=60
# )
# matching_hosts = [h for h in hosts if filter1.matches_host(h)]
# print([h.name for h in matching_hosts])
