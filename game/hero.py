from random import randint
from typing import Optional

from game.Models.personage_models import Hero


class Enemy(Hero):
    def hit(self, target: Hero) -> Optional[float]:
        if randint(0, 100) < 10 and self.stamina >= self.class_.skill.stamina and not self.skill_used:
            self.use_skill()
        return self._hit(target)


class Player(Hero):
    def hit(self, target: Hero) -> Optional[float]:
        return self._hit(target)
