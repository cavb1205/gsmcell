from app import db
from app.almacen.models import Almacen


class Inversion(db.Model):
    __tablename__ = 'inversiones'

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Float,nullable=False)
    description = db.Column(db.String(200),nullable=False)
    almacen_id = db.Column(db.Integer, db.ForeignKey('almacenes.id'),nullable=False)

    def __str__(self):
        return self.description
    

