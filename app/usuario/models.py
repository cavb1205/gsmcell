from app import db

class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    rut = db.Column(db.String(12), unique=True, nullable=False)
    username = db.Column(db.String(80), unique=True)
    first_name = db.Column(db.String(100),nullable=False)
    last_name = db.Column(db.String(100),nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128))
    cel = db.Column(db.String(12),nullable=False)
    cel_opt = db.Column(db.String(12))
    is_active = db.Column(db.Boolean, default=True)
    is_admin = db.Column(db.Boolean, default=False)
    almacen_id = db.Column(db.Integer, db.ForeignKey('almacenes.id'),nullable=False)

    def __repr__(self):
        return '<User %r>' % self.first_name


        