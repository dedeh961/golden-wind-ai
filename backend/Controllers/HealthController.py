from flask import Blueprint, jsonify
from flask.views import MethodView

blp = Blueprint("healthview", __name__)


class HealthController(MethodView):
    def get(self):
        return jsonify({"status": "ok"})


healthview = HealthController.as_view("healthview")

blp.add_url_rule("/health", view_func=healthview)
