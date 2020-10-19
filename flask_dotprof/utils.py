from pathlib import Path

from flask.helpers import send_file
from flask.wrappers import Response


def serve_frontend_resource(path: str) -> Response:
    return send_file(Path(__file__).parent / "frontend" / "build" / path)
