from include.models import User, Articulos
from run import db



def get_user_by_email(correo):
    user = User.query.filter_by(correoUsuario=correo).first()
    return user

def get_articulos_user_by_id(id_user):
    articulos_user = Articulos.query.filter_by(idUsuario=id_user).all()
    return articulos_user

def update_articulo(id_articulo,titulo,articulo_nuevo):
    articulo = Articulos.query.filter(Articulos.id==id_articulo).first()
    articulo.nombreArticulo= titulo
    articulo.articulo = articulo_nuevo
    db.session.add(articulo)
    db.session.commit()

def get_articulo_by_id(id_articulo):
    articulo = Articulos.query.filter(Articulos.id==id_articulo).first()
    return articulo

