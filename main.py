# main.py

from flask import Blueprint, render_template, request, json, redirect, url_for
from flask_login import login_required, current_user
from include.models import Articulos
from run import db
from include.DAO import get_articulos_by_id

main = Blueprint('main', __name__, url_prefix= '')

@main.route('/')
def index():
    return render_template('accounts/login.html')

@main.route('/profile')
@login_required
def profile():
    if current_user.tipoUsuario == 'Trader':
        return render_template('accounts/profile_trader.html', name=current_user.nombreUsuario, segment='profile')
    else:
        return redirect(url_for('main.profile_investigador'))

@main.route('/profile_investigador')
@login_required
def profile_investigador():
    articulos_user = get_articulos_by_id(current_user.id)

    return render_template('accounts/profile_invest.html', nombre=current_user.nombreUsuario, segment='profile', articulos_user=articulos_user)

@main.route('/profile_investigador', methods=['POST'])
@login_required
def profile_investigador_post():
    publicación = request.form['publicación']
    titulo = request.form['titulo']
    nuevo_articulo= Articulos(nombreArticulo=titulo, autorArticulo=current_user.nombreUsuario,articulo=publicación,noEdicion=1,estatusArticulo=1,idUsuario=current_user.id)
    db.session.add(nuevo_articulo)
    db.session.commit()
    articulos_user= get_articulos_by_id(current_user.id)
 
    return render_template('accounts/profile_invest.html', name=current_user.nombreUsuario, segment='profile', articulos_user=articulos_user)