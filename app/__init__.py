from flask import Flask
from flask_sqlalchemy import SQLAlchemy



db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
  
  
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://root:c@m1lovaron@localhost/gsmcell'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['debug']=False

    #blueprints
    from app.usuario import usuario
    from app.almacen import almacen

    app.register_blueprint(almacen)
    app.register_blueprint(usuario)



    return app