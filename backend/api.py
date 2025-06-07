import logging
import os

from Controllers.AskController import blp as AskBlueprint
from Controllers.HealthController import blp as HealthBlueprint
from dotenv import dotenv_values
from flask import Flask
from Services.PullModelService import PullModelService


def create_app():
    app = Flask(__name__)

    variaveis_de_ambiente = {
        **dotenv_values(".env.development"),
        **os.environ,
    }

    app.config.update(variaveis_de_ambiente)

    app.register_blueprint(AskBlueprint)
    app.register_blueprint(HealthBlueprint)

    logging.basicConfig(level=logging.DEBUG)

    with app.app_context():
        PullModelService().run("llama3.2")
        PullModelService().run("nomic-embed-text")

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=80)
