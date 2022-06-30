from typing import Optional, Type

from game.Models.game import GameSingletonMeta
from game.Models.personage_models import Hero
from game.hero import Player


class Game(metaclass=GameSingletonMeta):
    def __init__(self) -> None:
        self.player = None
        self.enemy = None
        self.game_processing = False
        self.game_results = ''

    def run(self, player: Hero, enemy: Hero) -> None:
        self.player = player
        self.enemy = enemy
        self.game_processing = True

    def _check_hp(self) -> Optional[str]:
        if self.player.hp <= 0 and self.enemy.hp <= 0:
            return self._end_game(results='в этой игре никто не победил')
        if self.player.hp <= 0:
            return self._end_game(results='Игрок проиграл')
        if self.enemy.hp <= 0:
            return self._end_game(results='Игрок победил')
        return None

    def _end_game(self, results: str) -> str:
        self.game_processing = False
        self.game_results = results
        return results

    def nex_turn(self) -> str:
        if results := self._check_hp():
            return results

        if not self.game_processing:
            return self.game_results

        results = self.enemy_hit()
        self._stamina_regenerate()
        return results

    def _stamina_regenerate(self) -> None:
        self.player.regenerate_stamina()
        self.enemy.regenerate_stamina()

    def enemy_hit(self) -> str:
        dealt_damage: Optional[float] = self.enemy.hit(self.player)
        if dealt_damage is not None:
            self.player.take_hit(dealt_damage)
            results = f'Враг наносит {dealt_damage} тебе'
        else:
            results = f'Враг не нанес урона'
        return results

    def player_hit(self) -> str:
        dealt_damage: Optional[float] = self.player.hit(self.player)

        if dealt_damage is not None:
            self.enemy.take_hit(dealt_damage)
            return f'Вы нанесли врагу {dealt_damage} урон<p>{self.nex_turn()}</p>'
        return f'Вы не нанесли урона, нету сил<p>{self.nex_turn()}</p>'

    def player_use_skill(self) -> str:
        dealt_damage: Optional[float] = self.player.use_skill()
        if dealt_damage is not None:
            self.enemy.take_hit(dealt_damage)
            return f'Вы нанесли врагу {dealt_damage} урон<p>{self.nex_turn()}</p>'
        return f'Вы не нанесли урона, не хватило сил<p>{self.nex_turn()}</p>'
