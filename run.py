from app import create_app, db
from flask import render_template, request
from flask_wtf import FlaskForm




app = create_app()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tipo-reparaciones/')
def comun():
    return render_template('comun-repair.html')


if __name__=='__main__':
    
    db.init_app(app)
    
    with app.app_context():
        from app.inversion.models import Inversion
        db.create_all()

    app.run(debug=True, host='0.0.0.0')