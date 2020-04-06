from flask import render_template, request,redirect,url_for
from app import db
from . import usuario

from .models import User
from app.almacen.models import Almacen

from .forms import UserForm



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


@usuario.route('new/', methods=['GET','POST'])
def usuario_create():
    '''view create user'''
    
    form = UserForm()
    if form.validate_on_submit():
        rut = form.rut.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        cel = form.cel.data
        cel_opt = form.cel_opt.data

        user = User(rut=rut, first_name=first_name, last_name=last_name,email=email,cel=cel,cel_opt=cel_opt, almacen_id=1 )
        print (user)
        db.session.add(user)
        db.session.commit()
        
        return redirect(url_for('usuario.usuario_list'))

    return render_template('usuario/usuario_form.html', form=form)


@usuario.route('update/<int:user_id>/', methods=['GET','POST'])
def usuario_update(user_id):
    """view user update"""

    user = User.query.get(user_id)
    form = UserForm(obj=user)
    if form.validate_on_submit():
        user.rut = form.rut.data
        user.first_name = form.first_name.data 
        user.last_name = form.last_name.data 
        user.email = form.email.data
        user.cel = form.cel.data
        user.cel_opt = form.cel_opt.data

        db.session.add(user)
        db.session.commit()
        return redirect(url_for('usuario.usuario_list'))

    return render_template('usuario/usuario_form.html', form=form) 

@usuario.route('delete/<int:user_id>/')
def usuario_delete(user_id):
    """view user delete"""

    user = User.query.get(user_id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('usuario.usuario_list'))