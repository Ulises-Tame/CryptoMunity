# models.py

from flask_login import UserMixin
from run import db

class User(UserMixin, db.Model):
    __tablename__ = 'Usuarios'
    id = db.Column('IdUsuario', db.Integer, primary_key=True)
    nombreUsuario = db.Column(db.String(100), nullable=False)
    apellidoUsuario = db.Column(db.String(100), nullable=False)
    telefonoUsuario = db.Column(db.String(100), nullable=False)
    correoUsuario = db.Column(db.String(250), unique=True, nullable=False)
    contrasena = db.Column(db.String(100))
    tipoUsuario = db.Column(db.String(250), nullable=False)
    estatusUsuario = db.Column(db.Integer, nullable=True)

class Articulos(db.Model):
    __tablename__ = 'Articulos'
    id = db.Column('IdArticulos',db.Integer, primary_key=True)
    nombreArticulo = db.Column(db.String(80), nullable=False)
    autorArticulo= db.Column(db.String(80), nullable=False)
    articulo = db.Column(db.Text, nullable=False)
    fechaDePublicacion= db.Column(db.Date, nullable=True)
    noEdicion = db.Column(db.Integer,nullable=False)
    estatusArticulo = db.Column(db.Integer, nullable=False)
    fechaEdicion = db.Column(db.Date, nullable=True)
    cryptoRelacionada = db.Column(db.String(20), nullable=False)
    idUsuario = db.Column(db.Integer, nullable=False)