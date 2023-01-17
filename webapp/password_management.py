import json
from flask import Blueprint, render_template, session, redirect, url_for
from database.database_passwords import get_user_passwords
from utils import login_required, UserDifferenceException

password_management = Blueprint('password_management', __name__,
                                template_folder='templates')


@password_management.route('/')
@login_required()
def password_main():
    return render_template('passwords_main.html')


@password_management.route('/view_passwords')
@login_required()
def view_passwords_main():
    try:
        user_passwords = get_user_passwords(session['email'])
        return render_template('view_passwords.html',
                               user_passwords=user_passwords)
    except UserDifferenceException:
        messages = {
            'message': 'There was an error getting your information.',
            'heading': 'Error',
            'type': 'danger'
        }

        return redirect(url_for('password_management.password_main',
                                messages=json.dumps(messages)))


@password_management.route('/create_password')
@login_required()
def create_password_main():
    pass
