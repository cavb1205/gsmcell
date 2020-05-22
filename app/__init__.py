from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap




db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    db.init_app(app)
    Bootstrap(app)
  
  
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://root:c@m1lovaron@localhost/gsmcell'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['debug']=False

    #config wtf
    app.config['SECRET_KEY'] = 'your-secret-key-gdgasdgñoashd{hoougasoudg'
    
    
    #register blueprints
    from app.usuario import usuario
    from app.almacen import almacen
    from app.inversion import inversion 

    app.register_blueprint(almacen)
    app.register_blueprint(usuario)
    app.register_blueprint(inversion)



    return app