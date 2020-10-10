import os
import subprocess
from typing import Any

from flask import Blueprint, current_app, jsonify

from .utils import serve_frontend_resource

api = Blueprint("flask_dotprof_api", __name__)


@api.route("/static/<path:path>")
def static(path: str) -> Any:
    return serve_frontend_resource("static/" + path)


@api.route("/profiles")
def get_profiles() -> Any:
    return jsonify(profiles=os.listdir(current_app.config["DOTPROF_PROFILE_PATH"]))


@api.route("/profiles/<string:name>")
def get_profile(name: str) -> Any:
    process = subprocess.run(
        [
            "gprof2dot",
            "-f",
            "pstats",
            os.path.join(current_app.config["DOTPROF_PROFILE_PATH"], name),
        ],
        capture_output=True,
    )
    process.check_returncode()
    svg = subprocess.run(["dot", "-Tsvg"], input=process.stdout, capture_output=True)
    svg.check_returncode()
    return svg.stdout.decode("utf8")


@api.route("/", defaults={"path": ""})
@api.route("/<path:path>")
def catch_all(path: Any) -> Any:
    return serve_frontend_resource("index.html")
