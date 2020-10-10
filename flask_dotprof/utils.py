import os
from pathlib import Path

from flask import abort
from flask.helpers import send_file
from flask.wrappers import Response


def is_safe_path(basedir: Path, path: Path) -> bool:
    return os.path.realpath(path).startswith(str(basedir))


def serve_frontend_resource(path: str) -> Response:
    base_path = Path(__file__).parent / "frontend" / "build"
    file_path = base_path / path
    if not is_safe_path(base_path, file_path):
        abort(404)
    return send_file(file_path)
