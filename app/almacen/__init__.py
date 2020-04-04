from flask import Blueprint

almacen = Blueprint('almacen', __name__,url_prefix='/almacen' ,template_folder='template', static_folder='static')

from . import views

