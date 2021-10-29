from include.models import User, Articulos, Eventos, Criptomonedas, Botones
from run import db
from flask_login import current_user
import datetime

def insert_trader(user):
    db.session.add(user)
    db.session.commit()
    db.session.close()

def insert_investigador(user):
    db.session.add(user)
    db.session.commit()
    db.session.close()

def get_user_by_email(correo):
    user = User.query.filter_by(correoUsuario=correo).first()
    return user

def get_articulos_user_by_id(id_user):
    articulos_user = Articulos.query.filter_by(idUsuario=id_user).all()
    return articulos_user

def update_articulo(id_articulo,titulo,articulo_nuevo, sentimiento):
    articulo = Articulos.query.filter(Articulos.id==id_articulo).first()
    articulo.nombreArticulo= titulo
    articulo.articulo = articulo_nuevo
    articulo.sentimiento = sentimiento
    articulo.fechaEdicion = datetime.datetime.today()
    db.session.add(articulo)
    db.session.commit()

def get_articulo_by_id(id_articulo):
    articulo = Articulos.query.filter(Articulos.id==id_articulo).first()
    return articulo

def get_articulos_by_crypto(crypto):
    articulos= Articulos.query.filter(Articulos.cryptoRelacionada==crypto).all()
    return articulos

def get_crypto(crypto):
    crypto= Criptomonedas.query.filter(Criptomonedas.link==crypto).all()
    return crypto

def insert_articulo(articulo):
    db.session.add(articulo)
    db.session.commit()


def get_boton(tipo):
    boton= Botones.query.filter(Botones.tipo==tipo).all()
    return boton