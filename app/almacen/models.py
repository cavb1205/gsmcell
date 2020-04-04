from sqlalchemy import Integer, String, Float
from sqlalchemy import Boolean, Column , ForeignKey

from sqlalchemy.orm import relationship

from app.usuario.models import User

from app import db

class Almacen(db.Model):
    __tablename__ = 'almacenes'

    id = Column(Integer, primary_key=True)
    name = Column(String(100),nullable=False)
    address = Column(String(200))
    city = Column(String(100))
    is_active = Column(Boolean, default=True)
    value = Column(Float, default=0)
    users = relationship('User', backref='almacenes', lazy=True)

    def __repr__(self):
        return '<User %r>' % self.name