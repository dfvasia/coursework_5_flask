from functools import wraps
from typing import Dict

from flask import Flask, request, render_template, redirect, url_for

from config import EQUIPMENT
from controler import Game
from game.Models.personage_models import Hero

from game.hero import Player
from game.personages import personage_class


app = Flask(__name__)
app.debug = True
app.url_map.strict_slashes = False
game = Game()
heroes: Dict[str, Hero] = dict()


def game_processing(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if game.game_processing:
            return func(*args, **kwargs)
        if game.game_results:
            return render_template('fight.html', heroes=heroes, result=game.game_results)
        return redirect(url_for('index'))
    return wrapper


def render_choose_personage_template(**kwargs) -> str:
    return render_template(
        'hero_choosing.html',
        classes=personage_class.values(),
        equipment=EQUIPMENT,
        **kwargs
    )


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
    return redirect(url_for('choose_enemy'))


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
    return redirect(url_for('start_fight'))


@app.route('/fight')
def start_fight():
    if 'player' in heroes and 'enemy' in heroes:
        game.run(**heroes)
        return render_template('fight.html', heroes=heroes, result='Бой начался')
    return redirect(url_for('index'))


@app.route('/fight/hit')
@game_processing
def hit():
    return render_template('fight.html', heroes=heroes, result=game.player_hit())


@app.route('/fight/use-skill')
@game_processing
def user_skill():
    return render_template('fight.html', heroes=heroes, result=game.player_use_skill())


@app.route('/fight/pass-turn')
@game_processing
def pass_turn():
    return render_template('fight.html', heroes=heroes, result=game.nex_turn())


@app.route('/fight/end-fight')
def end_fight():
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
