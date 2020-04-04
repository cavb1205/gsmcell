from flask import Blueprint

usuario = Blueprint('usuario', __name__,url_prefix='/usuario' ,template_folder='template', static_folder='static')

from . import views
