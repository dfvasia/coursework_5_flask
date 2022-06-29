from flask import Flask, request, render_template, redirect, url_for

from game.Models.equipment_models import EquipmentData
from game.personages import personage_class
from game.utils import load_equipment

equipment: EquipmentData = load_equipment()

print(equipment)


def render_choose_personage_template(**kwargs) -> str:
    return render_template(
        'hero_choosing.html',
        classes=personage_class.values(),
        equipment=equipment,
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
        return redirect(url_for('choose-enemy'))

    @app.route('/choose-enemy', methods=['GET', 'POST'])
    def choose_enemy():
        if request.method == 'GET':
            return render_choose_personage_template(
                header='Выберите врага',
                next_button='Начать сражение'
            )
        return '<h2>Not implemented</h2>'
    return app
