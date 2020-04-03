
from flask import Flask, render_template, request

from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://root:c@m1lovaron@localhost/gsmcell'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from models import User




@app.route('/')
def index():
    return render_template('base.html')

@app.route('/inversion/')
def inversion_list():
    inversion_list = [200,400,600,543]
    context = {'inversion_list':inversion_list}
    return render_template('inversion/inversion_list.html', **context)


@app.route('/usuario/')
def usuario_list():
    usuario_list = User.query.all()
    context = {'usuario_list':usuario_list}
    return render_template('usuario/usuario_list.html', **context)