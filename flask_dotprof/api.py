from typing import Any

from flask import Blueprint, jsonify

api = Blueprint("flask_dotprof_api", __name__)


@api.route("/test")
def test() -> Any:
    return jsonify(test=True), 418
