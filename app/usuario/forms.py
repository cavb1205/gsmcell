from flask_wtf import FlaskForm

from wtforms import StringField, IntegerField, BooleanField,SelectField, SubmitField
from wtforms.validators import DataRequired, Email, Length

from app.almacen.models import Almacen






class UserForm(FlaskForm):
    rut = StringField('Rut', validators=[DataRequired(message='Este campo no puede estar vacio'),Length(min=8, max=12, message='Debe tener entre 8 y 12 dígitos')])
    first_name = StringField('Nombres', validators=[DataRequired(),Length(min=2, max=100,message='Debe tener min 4 dígitos')])
    last_name = StringField('Apellidos', validators=[DataRequired(),Length(min=2, max=100,message='Debe tener min 4 dígitos')])
    email = StringField('Email', validators=[DataRequired(),Email(message='Ingrese un Email válido'),Length(min=2, max=120,message='Ingrese un Email válido')])
    cel = StringField('Celular', validators=[DataRequired(),Length(min=8, max=12, message='Ingrese Número Válido +56 9  ')])
    cel_opt = StringField('Celular Opcional')
    
    submit = SubmitField('Registrar')