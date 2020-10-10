import time
from typing import Any

from flask import Flask

from flask_dotprof import FlaskDotprof

app = Flask(__name__)
app.config["DOTPROF_PROFILE_PATH"] = "test_app/profiles/"
dotprof = FlaskDotprof(app)


def function_a() -> None:
    for i in range(10):
        function_b()
    for i in range(3):
        function_c()


def function_b() -> None:
    time.sleep(0.025)


def function_c() -> None:
    time.sleep(0.25)
    function_b()


@app.route("/test")
def test_route() -> Any:
    function_a()
    return ""


app.run()
