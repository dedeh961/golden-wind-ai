from flask import Blueprint, jsonify, request
from flask.views import MethodView
from Services.AskService import AskService

blp = Blueprint("askview", __name__)


class AskController(MethodView):
    def post(self):
        question = request.json.get("question")

        response = AskService().run(question)

        return jsonify({"answer": response})


askview = AskController.as_view("askview")

blp.add_url_rule("/ask", view_func=askview)
