import shutil
from pathlib import Path
from typing import Optional

from flask import Flask
from werkzeug.middleware.profiler import ProfilerMiddleware

from .api import api


class FlaskDotprof:
    def __init__(self, app: Optional[Flask]) -> None:
        self.app = app

        if shutil.which("dot") is None:
            # TODO: Return dot straight to frontend, use d3 to render
            raise RuntimeError(
                "Unable to locate dot. Please ensure graphviz is installed and "
                "available on your path."
            )

        if app is not None:
            self.init_app(app)

    def init_app(self, app: Flask) -> None:
        profile_path = app.config["DOTPROF_PROFILE_PATH"]

        Path(profile_path).mkdir(parents=True, exist_ok=True)

        setattr(
            app,
            "wsgi_app",
            ProfilerMiddleware(
                app.wsgi_app,
                stream=None,  # type: ignore
                profile_dir=profile_path,
            ),
        )

        app.register_blueprint(api, url_prefix="/dotprof")
