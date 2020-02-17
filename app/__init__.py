from flask import Flask
from flask.helpers import get_env

from . import api, view

app = Flask(__name__, static_folder='../static', template_folder='../static/templates')

app.register_blueprint(api.bp)
app.register_blueprint(view.bp)

app.config.from_object('config.{}'.format(get_env().capitalize()))
