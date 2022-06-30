from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Type, Optional

from config import BASE_STAMINA_PER_ROUND
from game.Models.equipment_models import Armor, Weapon
from game.Models.skill_models import Skill


class Personage(ABC):

    name: str = NotImplemented
    max_health: float = NotImplemented
    max_stamina: float = NotImplemented
    stamina_modifier: float = NotImplemented
    attack_modifier: float = NotImplemented
    armor_modifier: float = NotImplemented
    skill: Skill = NotImplemented


class Hero(ABC):
    def __init__(self, class_: Type[Personage], weapon: Weapon, armor: Armor, name: str):
        self.class_ = class_
        self.weapon = weapon
        self.armor = armor
        self._stamina = self.class_.max_stamina
        self._hp = self.class_.max_health
        self.skill_used: bool = False
        self.name = name

    @property
    def hp(self):
        return round(self._hp, 1)

    @hp.setter
    def hp(self, value):
        self._hp = value

    @property
    def stamina(self):
        return round(self._stamina, 1)

    @stamina.setter
    def stamina(self, value):
        self._stamina = value

    @property
    def _total_armor(self) -> float:
        if self.stamina - self.armor.stamina_per_turn >= 0:
            return self.armor.defence * self.class_.armor_modifier
        return 0

    def _hit(self, target: Hero) -> Optional[float]:
        if self.stamina - self.weapon.stamina_per_hit < 0:
            return None

        hero_damage = self.weapon.damage * self.class_.attack_modifier
        dealt_damage = hero_damage - target._total_armor
        if dealt_damage < 0:
            return 0
        self.stamina -= self.weapon.stamina_per_hit
        return round(dealt_damage, 1)

    def take_hit(self, damage: float):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def regenerate_stamina(self):
        delta_stamina = BASE_STAMINA_PER_ROUND * self.class_.stamina_modifier
        if self.stamina + delta_stamina <= self.class_.max_stamina:
            self.stamina += delta_stamina
        else:
            self.stamina = self.class_.max_stamina

    def use_skill(self) -> Optional[float]:
        if not self.skill_used and self.stamina - self.class_.max_stamina:
            self.skill_used = True
            return round(self.class_.skill.damage, 1)
        return None

    @abstractmethod
    def hit(self, target: Hero) -> Optional[float]:
        ...
