# main.py

from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from models import Articulos
from run import db

main = Blueprint('main', __name__, url_prefix= '')

@main.route('/')
def index():
    return render_template('accounts/login.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('accounts/profile_trader.html', name=current_user.nombreUsuario, segment='profile')

@main.route('/profile_investigador')
@login_required
def profile_investigador():
    return render_template('accounts/profile_invest.html', name=current_user.nombreUsuario, segment='profile')

@main.route('/profile_investigador', methods=['POST'])
@login_required
def profile_investigador_post():
    publicación = request.form['publicación']
    titulo = request.form['titulo']
    
    nuevo_articulo= Articulos(nombreArticulo=titulo, autorArticulo=current_user.nombreUsuario,articulo=publicación,noEdicion=1,estatusArticulo=1,idUsuario=current_user.id)
    print (publicación, titulo)
    db.session.add(nuevo_articulo)
    db.session.commit()
    fila=[titulo,publicación]
 
    return render_template('accounts/profile_invest.html', name=current_user.nombreUsuario, segment='profile')