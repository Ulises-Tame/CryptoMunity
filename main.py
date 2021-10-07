# main.py

from flask import Blueprint, render_template, request, json, redirect, url_for
from flask_login import login_required, current_user
from include.models import Articulos
from run import db
from include.DAO import get_articulos_user_by_id, update_articulo, get_articulo_by_id, get_articulos_by_crypto

main = Blueprint('main', __name__, url_prefix= '')

def check_user():
    if current_user.tipoUsuario == 'Trader':
        return True
    else:
        return None

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

@main.route('/art-trader/<string:crypto>')
@login_required
def articulos_trader(crypto):
    user = check_user()
    if  user:
        pass
    else: 
        return redirect(url_for('main.profile'))
    print(crypto)
    articulos = get_articulos_by_crypto(crypto)
    print(articulos)
    return render_template('accounts/trader_articulos.html', name=current_user.nombreUsuario, segment='profile', articulos_crypto=articulos)

@main.route('/profile_investigador')
@login_required
def profile_investigador():
    user = check_user()
    if user:
        return redirect(url_for('main.profile'))
    articulos_user = get_articulos_user_by_id(current_user.id)
    for articulos in articulos_user:
        print(articulos.fechaDePublicacion)

    return render_template('accounts/profile_invest.html', nombre=current_user.nombreUsuario, segment='profile', articulos_user=articulos_user)

@main.route('/articulos')
@login_required
def articulos():
    user = check_user()
    if user:
        return redirect(url_for('main.profile'))
    return render_template('accounts/agregar_articulo.html', nombre=current_user.nombreUsuario, segment='articulos')

@main.route('/articulos', methods=['POST'])
@login_required
def articulos_post():
    user = check_user()
    if user:
        return redirect(url_for('main.profile'))
    publicación = request.form['publicación']
    titulo = request.form['titulo']
    crypto = request.form['crypto']
    print(crypto)
    nuevo_articulo= Articulos(nombreArticulo=titulo, autorArticulo=current_user.nombreUsuario,articulo=publicación,noEdicion=1,estatusArticulo=1,cryptoRelacionada=crypto,idUsuario=current_user.id)
    db.session.add(nuevo_articulo)
    db.session.commit()
 
    return render_template('accounts/agregar_articulo.html', name=current_user.nombreUsuario, segment='articulos')


@main.route('/articulos/edit/<int:id>')
@login_required
def articulos_edit(id):
    user = check_user()
    if user:
        return redirect(url_for('main.profile'))
    articulo = get_articulo_by_id(id)
    return render_template('accounts/editar.html', segment='articulos', articulo=articulo)

@main.route('/articulos/edit/<int:id>', methods=['POST'])
@login_required
def articulos_edit_post(id):
    user = check_user()
    if user:
        return redirect(url_for('main.profile'))
    publicación = request.form['publicación']
    titulo = request.form['titulo']
    update_articulo(id,titulo,publicación)
    return redirect(url_for('main.profile'))