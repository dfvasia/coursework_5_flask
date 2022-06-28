from abc import ABC
import weakref

from game.Models.skill_models import Skill


# class PersonageMeta(type):
#     def __init__(cls, *args, **kwargs):
#         cls.__instances = {}
#         super(PersonageMeta, cls).__init__(*args, **kwargs)
#
#     def get_instances(self):
#         return list(self.__instances.values())
#
#     def delete(self, id_instance):
#         del self.__instances[id_instance]
#
#     def __call__(cls, *args, **kwargs):
#         instance = super(PersonageMeta, cls).__call__(*args, **kwargs)
#         cls.__instances[id(instance)] = weakref.proxy(instance)
#         return instance


# class Personage(ABC, metaclass=PersonageMeta):
class Personage(ABC):
    name: str = NotImplemented
    health: float = NotImplemented
    stamina: float = NotImplemented
    stamina_modifier: float = NotImplemented
    attack_modifier: float = NotImplemented
    armor_modifier: float = NotImplemented
    skill: Skill = NotImplemented

    # def __del__(self):
    #     self.__class__.delete(id(self))
