from typing import Dict, Type

from flask import Flask, request, render_template, redirect, url_for

from game.Models.equipment_models import EquipmentData
from game.Models.personage_models import Hero
from game.hero import Player
from game.personages import personage_class
from game.utils import load_equipment

EQUIPMENT: EquipmentData = load_equipment()

heroes: Dict[str, Hero] = dict()


def render_choose_personage_template(**kwargs) -> str:
    return render_template(
        'hero_choosing.html',
        classes=personage_class.values(),
        equipment=EQUIPMENT,
        **kwargs,
    )


def create_app(config_obj):
    app = Flask(__name__)
    app.config.from_object(config_obj)

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/choose-hero', methods=['GET', 'POST'])
    def choose_hero():
        if request.method == 'GET':
            return render_choose_personage_template(
                header='Выберите героя',
                next_button='Выбрать врага',
            )
        heroes['player'] = Player(
            class_=personage_class[request.form['unit_class']],
            weapon=EQUIPMENT.get_weapon(request.form['weapon']),
            armor=EQUIPMENT.get_armor(request.form['armor']),
            name=request.form['name']
        )
        return redirect(url_for('choose-enemy'))

    @app.route('/choose-enemy', methods=['GET', 'POST'])
    def choose_enemy():
        if request.method == 'GET':
            return render_choose_personage_template(
                header='Выберите врага',
                next_button='Начать сражение'
            )
        heroes['enemy'] = Player(
            class_=personage_class[request.form['unit_class']],
            weapon=EQUIPMENT.get_weapon(request.form['weapon']),
            armor=EQUIPMENT.get_armor(request.form['armor']),
            name=request.form['name']
        )
        return '<h2>Not implemented</h2>'

    @app.route('/fight')
    def start_fight():
        if 'player' in heroes and 'enemy' in heroes:
            return render_template('fight.html', heroes=heroes, results='Fight!')
        return redirect(url_for('index'))
    return app
