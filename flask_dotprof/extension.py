from pathlib import Path
from typing import Optional

from flask import Flask
from werkzeug.middleware.profiler import ProfilerMiddleware

from .api import api


class FlaskDotprof:
    def __init__(
        self, app: Optional[Flask], profile_path: Optional[str] = None
    ) -> None:
        self.app = app
        self._profile_path = profile_path

        if app is not None:
            self.init_app(app)

    def init_app(self, app: Flask) -> None:
        self._profile_path = self._profile_path or app.config["DOTPROF_PROFILE_PATH"]

        Path(self._profile_path).mkdir(parents=True, exist_ok=True)

        setattr(
            app,
            "wsgi_app",
            ProfilerMiddleware(
                app.wsgi_app,
                stream=None,  # type: ignore
                profile_dir=self._profile_path,
            ),
        )

        app.register_blueprint(api, url_prefix="/dotprof")
