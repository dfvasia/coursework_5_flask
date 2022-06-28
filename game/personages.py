from game.Models.personage_models import Personage
from game.Models.skill_models import Skill
from game.skills import ferocious_kick, powerful_thrust


class Warrior(Personage):
    name = 'Воин'
    health = 60.0
    stamina = 30.0
    stamina_modifier = 0.9
    attack_modifier = 0.8
    armor_modifier = 1.2
    skill = ferocious_kick


class Thief(Personage):
    name = 'Вор'
    health = 50.0
    stamina = 25.0
    stamina_modifier = 1.2
    attack_modifier = 1.5
    armor_modifier = 1.0
    skill = powerful_thrust
