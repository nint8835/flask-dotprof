from typing import Optional

from flask import Flask


class FlaskDotprof:
    def __init__(self, app: Optional[Flask]) -> None:
        self.app = app

        if app is not None:
            self.init_app(app)

    def init_app(self, app: Flask) -> None:
        pass
