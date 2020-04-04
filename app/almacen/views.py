from flask import render_template


from app.almacen import almacen

from .models import Almacen



@almacen.route('/')
def almacen_list():
    """return list almacen"""
    print('ingresa a list almacen')
    almacen_list = Almacen.query.all()
    return render_template('almacen/almacen_list.html', almacen_list=almacen_list)