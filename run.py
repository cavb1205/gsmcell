from app import create_app, db
from flask import render_template, request
from flask_wtf import FlaskForm




app = create_app()


@app.route('/')
def index():
    return render_template('index.html')


if __name__=='__main__':
    
    db.init_app(app)
    with app.app_context():
        db.create_all()

    app.run(debug=True)