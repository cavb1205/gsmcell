from flask import Blueprint

inversion = Blueprint('inversion', __name__, url_prefix='/inversion',template_folder='template', static_folder='static')

from . import views
