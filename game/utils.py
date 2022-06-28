import json
import os
from typing import Union
import marshmallow_dataclass

from exceptions import FileDoesNotExist, StructureIsNotCorrect
from game.Models.equipment_models import EquipmentData

BASE_DIR: str = os.path.abspath(os.path.dirname(__file__))
EQUIPMENT_PATH: str = os.path.join(BASE_DIR, 'game', 'data', 'equipment.json')


def read_json(file_path: str, encoding: str = 'utf-8') -> Union[dict, list]:
    try:
        with open(file_path, encoding=encoding) as f:
            return json.load(f)
    except Exception:
        raise FileDoesNotExist


def load_equipment() -> EquipmentData:
    try:
        return marshmallow_dataclass.class_schema(EquipmentData)().load(data=read_json(EQUIPMENT_PATH))
    except Exception:
        raise StructureIsNotCorrect