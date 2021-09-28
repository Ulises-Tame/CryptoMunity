from include.models import User, Articulos



def get_user_by_email(correo):
    user = User.query.filter_by(correoUsuario=correo).first()
    return user

def get_articulos_by_id(id_user):
    articulos_user = Articulos.query.filter_by(idUsuario=id_user).all()
    return articulos_user
