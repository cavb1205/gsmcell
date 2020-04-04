from flask import render_template

from . import usuario

from .models import User



@usuario.route('/')
def usuario_list():
    usuario_list = User.query.all() 
    print (usuario_list)
    context = {'usuario_list':usuario_list}
    return render_template('usuario/usuario_list.html', **context)