from flask import Flask


def create_app(config_obj):
    app = Flask(__name__)
    app.config.from_object(config_obj)

    return app
