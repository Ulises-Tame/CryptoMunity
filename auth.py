# auth.py

from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from models import User
from run import db

auth = Blueprint('auth', __name__, url_prefix= '')

@auth.route('/login')
def login():
    return render_template('accounts/login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    correo = request.form.get('correo')
    contraseña = request.form.get('contraseña')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(correoUsuario=correo).first()

    # check if user actually exists
    # take the user supplied password, hash it, and compare it to the hashed password in database
    if not user or not check_password_hash(user.contrasena, contraseña): 
        
        return render_template('accounts/login.html',
                               msg='Correo o Contraseña invalidos') # if user doesn't exist or password is wrong, reload the page

    # if the above check passes, then we know the user has the right credentials
    login_user(user, remember=remember)
    if user.tipoUsuario=='Trader': 
        return redirect(url_for('main.profile'))
    else:
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
    
    user = User.query.filter_by(correoUsuario=correo).first() # if this returns a user, then the email already exists in database

    if user: # if a user is found, we want to redirect back to signup page so user can try again  
        
        return render_template('accounts/register.html',
                               msg='Ese correo ya existe')

    # create new user with the form data. Hash the password so plaintext version isn't saved.
    new_user = User(correoUsuario=correo, nombreUsuario=nombre,apellidoUsuario=apellido,telefonoUsuario=telefono, contrasena=generate_password_hash(contraseña, method='sha256'), tipoUsuario='Trader', estatusUsuario=1)

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()
    db.session.close()

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
    
    user = User.query.filter_by(correoUsuario=correo).first() # if this returns a user, then the email already exists in database

    if user: # if a user is found, we want to redirect back to signup page so user can try again  
        
        return render_template('accounts/register_invest.html',
                               msg='Ese correo ya existe')

    # create new user with the form data. Hash the password so plaintext version isn't saved.
    new_user = User(correoUsuario=correo, nombreUsuario=nombre,apellidoUsuario=apellido,telefonoUsuario=telefono, contrasena=generate_password_hash(contraseña, method='sha256'), tipoUsuario='Investigador', estatusUsuario=1)

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()
    db.session.close()

    return render_template('accounts/login.html', msg='¡Listo! Cuenta Creada' )

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))