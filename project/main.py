# main.py

from flask import Blueprint, render_template
from flask_login import login_required, current_user

main = Blueprint('main', __name__, url_prefix= '')

@main.route('/')
def index():
    return render_template('accounts/login.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('accounts/profile_trader.html', name=current_user.nombreUsuario, segment='profile')