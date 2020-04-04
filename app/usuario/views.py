from flask import render_template, request

from . import usuario

from .models import User



@usuario.route('/')
def usuario_list():
    usuario_list = User.query.all() 
    print (usuario_list)
    context = {'usuario_list':usuario_list}
    return render_template('usuario/usuario_list.html', **context)


@usuario.route('<int:user_id>/')
def usuario_detail(user_id):
    """user detail view"""
    user = User.query.get(user_id)
    print(user.first_name)
    return render_template('usuario/usuario_detail.html', user=user)


@usuario.route('new/', methods=['POST', 'GET'])
def usuario_cretate():
    """view create user"""

    #if request.method == 'POST':
    
    pass

#    return render_template('usuario/usuario_form.html', form=form)