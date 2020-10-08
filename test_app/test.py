from flask_dotprof import FlaskDotprof
from flask import Flask

app = Flask(__name__)
dotprof = FlaskDotprof(app)
