# auth.py

from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from include.models import User
from run import db
from include.DAO import( get_user_by_email, 
insert_trader, 
insert_investigador
) 
from include.DAO_EVENTOS import (insert_error_login, 
insert_error_registrar, 
insert_evento_registro,
insert_evento_logout,
insert_evento_login
) 


auth = Blueprint('auth', __name__, url_prefix= '')

@auth.route('/login')
def login():
    return render_template('accounts/login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    correo = request.form.get('correo')
    contraseña = request.form.get('contraseña')
    remember = True if request.form.get('remember') else False

    user = get_user_by_email(correo)

    # check if user actually exists
    # take the user supplied password, hash it, and compare it to the hashed password in database
    if not user or not check_password_hash(user.contrasena, contraseña):
        insert_error_login('error','error')
        return render_template('accounts/login.html',
                               msg='Correo o Contraseña invalidos') # if user doesn't exist or password is wrong, reload the page

    # if the above check passes, then we know the user has the right credentials
    login_user(user, remember=remember)
    if user.tipoUsuario=='Trader':
        insert_evento_login()
        return redirect(url_for('main.profile'))
    else:
        insert_evento_login()
        return redirect(url_for('main.profile_investigador'))

@auth.route('/signup')
def signup():
    return render_template('accounts/register.html')

@auth.route('/signup', methods=['POST'])
def signup_post():

    nombre = request.form['nombre']
    apellido = request.form['apellido']
    telefono = request.form['telefono']
    contraseña = request.form['contraseña']
    correo = request.form['correo']
    tipo = 'Trader'
    
    user = get_user_by_email(correo) # if this returns a user, then the email already exists in database

    if user: # if a user is found, we want to redirect back to signup page so user can try again
        insert_error_registrar('error','error')
        return render_template('accounts/register.html',
                               msg='Ese correo ya existe')

    # create new user with the form data. Hash the password so plaintext version isn't saved.
    new_user = User(correoUsuario=correo, nombreUsuario=nombre,apellidoUsuario=apellido,telefonoUsuario=telefono, contrasena=generate_password_hash(contraseña, method='sha256'), tipoUsuario=tipo, estatusUsuario=1)

    # add the new user to the database
    insert_trader(new_user)
    user = get_user_by_email(correo)
    user_id = user.id
    insert_evento_registro(user_id,tipo)
    return render_template('accounts/login.html', msg='¡Listo! Cuenta Creada' )

@auth.route('/investigador')
def investigador():
    return render_template('accounts/register_invest.html')

@auth.route('/investigador', methods=['POST'])
def investigador_post():

    nombre = request.form['nombre']
    apellido = request.form['apellido']
    telefono = request.form['telefono']
    contraseña = request.form['contraseña']
    correo = request.form['correo']
    tipo = 'Investigador'
    
    user = get_user_by_email(correo) # if this returns a user, then the email already exists in database

    if user: # if a user is found, we want to redirect back to signup page so user can try again  
        insert_error_registrar('error','error')
        return render_template('accounts/register_invest.html',
                               msg='Ese correo ya existe')

    # create new user with the form data. Hash the password so plaintext version isn't saved.
    new_user = User(correoUsuario=correo, nombreUsuario=nombre,apellidoUsuario=apellido,telefonoUsuario=telefono, contrasena=generate_password_hash(contraseña, method='sha256'), tipoUsuario=tipo, estatusUsuario=1)

    # add the new user to the database
    insert_investigador(new_user)
    user = get_user_by_email(correo)
    user_id = user.id
    insert_evento_registro(user_id,tipo)  
    return render_template('accounts/login.html', msg='¡Listo! Cuenta Creada' )

@auth.route('/logout')
@login_required
def logout():
    insert_evento_logout()
    logout_user()
    return redirect(url_for('main.index'))