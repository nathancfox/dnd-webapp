import os

from flask import Flask
from . import charactersheet


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.debug = True

    app.register_blueprint(charactersheet.bp)


    return app
