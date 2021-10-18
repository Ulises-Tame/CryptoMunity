from include.models import User, Articulos, Eventos
from run import db
from flask_login import current_user


def insert_evento_perfil():
    new_evento = Eventos(nombre_evento = "evento_perfil",idUsuario=current_user.id,tipoUsuario=current_user.tipoUsuario)
    db.session.add(new_evento)
    db.session.commit()

def insert_evento_login():
    new_evento = Eventos(nombre_evento = "evento_login",idUsuario=current_user.id,tipoUsuario=current_user.tipoUsuario)
    db.session.add(new_evento)
    db.session.commit()

def insert_error_login():
    new_error=Eventos(nombre_evento = "error_email_contraseña_mal",idUsuario=current_user.id,tipoUsuario=current_user.tipoUsuario)
    db.session.add(new_error)
    db.session.commit()

def insert_error_registrar():
    new_error=Eventos(nombre_evento = "error_email_existe",idUsuario=current_user.id,tipoUsuario=current_user.tipoUsuario)
    db.session.add(new_error)
    db.session.commit()

def insert_evento_registro():
    new_evento = Eventos(nombre_evento = "evento_registrar",idUsuario=current_user.id,tipoUsuario=current_user.tipoUsuario)
    db.session.add(new_evento)
    db.session.commit()

def insert_evento_logout():
    new_evento = Eventos(nombre_evento = "evento_logout",idUsuario=current_user.id,tipoUsuario=current_user.tipoUsuario)
    db.session.add(new_evento)
    db.session.commit()

def insert_evento_articulo():
    new_evento = Eventos(nombre_evento = "evento_vista_agregar_articulo",idUsuario=current_user.id,tipoUsuario=current_user.tipoUsuario)
    db.session.add(new_evento)
    db.session.commit()

def insert_evento_nuevoarticulo():
    new_evento = Eventos(nombre_evento = "evento_agregar_articulo",idUsuario=current_user.id,tipoUsuario=current_user.tipoUsuario)
    db.session.add(new_evento)
    db.session.commit()

def insert_vista_editararticulo():
    new_evento = Eventos(nombre_evento = "evento_vista_editar_articulo",idUsuario=current_user.id,tipoUsuario=current_user.tipoUsuario)
    db.session.add(new_evento)
    db.session.commit()

def insert_evento_editararticulo():
    new_evento = Eventos(nombre_evento = "evento_editar_articulo",idUsuario=current_user.id,tipoUsuario=current_user.tipoUsuario)
    db.session.add(new_evento)
    db.session.commit()

def insert_evento_crypto():
    new_evento = Eventos(nombre_evento = "evento_ver_crypto",idUsuario=current_user.id,tipoUsuario=current_user.tipoUsuario)
    db.session.add(new_evento)
    db.session.commit()


    
        