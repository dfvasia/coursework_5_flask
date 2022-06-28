from abc import ABC

from game.Models.skill_models import Skill


class Personage(ABC):
    name: str = NotImplemented
    health: float = NotImplemented
    stamina: float = NotImplemented
    stamina_modifier: float = NotImplemented
    attack_modifier: float = NotImplemented
    armor_modifier: float = NotImplemented
    skill: Skill = NotImplemented



