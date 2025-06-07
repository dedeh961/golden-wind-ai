import requests as rq
from flask import current_app


class PullModelService:
    def __init__(self):
        self.url_olhama = current_app.config["OLLAMA_URL"]
        self.url_pull_olhama = self.url_olhama + "/api/pull"

    def run(self, model_name: str) -> None:
        data = {"name": model_name}

        rq.post(self.url_pull_olhama, json=data)
