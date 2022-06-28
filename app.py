from flask import Flask, request, render_template

from cofig import DevelopmentConfig
from server import create_app


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!((((('


@app.route('/choose-hero', methods=['GET', 'POST'])
def choose_hero():
    if request.method == 'GET':
        render_template(
            'hero_choosing.html',
            header='Выберите героя',
        )


app = create_app(DevelopmentConfig)
