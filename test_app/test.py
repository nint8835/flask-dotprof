from flask import Flask

from flask_dotprof import FlaskDotprof

app = Flask(__name__)
app.config["DOTPROF_PROFILE_PATH"] = "test_app/profiles/"
dotprof = FlaskDotprof(app)

app.run()
