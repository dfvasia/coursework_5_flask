from dataclasses import dataclass
from random import uniform
from typing import List

from exceptions import ThingDoesntExist


@dataclass
class Weapon:
    id: int
    name: str
    min_damage: float
    max_damage: float
    stamina_per_hit: float

    def damage(self) -> float:
        return uniform(self.min_damage, self.max_damage)


@dataclass
class Armor:
    id: int
    name: str
    defence: float
    stamina_per_turn: float


@dataclass
class EquipmentData:
    weapons: List[Weapon]
    armors:  List[Armor]

    def get_weapon(self, weapons_name: str) -> Weapon:
        for weapon in self.weapons:
            if weapons_name == weapon.name:
                return weapon
            raise ThingDoesntExist

    def get_armor(self, armor_name: str) -> Armor:
        for armor in self.armors:
            if armor_name == armor.name:
                return armor
            raise ThingDoesntExist

    @property
    def weapon_names(self) -> List[str]:
        return [item.name for item in self.weapons]

    @property
    def armor_names(self) -> List[str]:
        return [item.name for item in self.armors]
