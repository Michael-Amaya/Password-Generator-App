import json
from flask import Blueprint, render_template, request, url_for, redirect, \
    session
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
from database.database_users import create_user, get_user_data, \
    change_user_password
from utils import message_capable
from settings import SETTINGS


login_register = Blueprint('login_register', __name__,
                           template_folder='templates')

# Login error message to stay consistent
login_error_message = 'There was an issue logging in!'


@login_register.route('/login_main', methods=['POST'])
def perform_login():
    user_data = request.form
    user_record = get_user_data(user_data['email'])
    if user_record is None:
        messages = {
            'message': login_error_message,
            'heading': 'Error',
            'type': 'danger'
        }

        return redirect(url_for('login_register.login_page',
                        messages=json.dumps(messages)))

    peppered_password = f"{user_data['password']}{SETTINGS['password_pepper']}"
    password_hasher = PasswordHasher()

    try:
        password_hasher.verify(user_record['password'], peppered_password)
        # Throws an exception if the password doesn't verify, so by this point,
        # we should be verified

        if password_hasher.check_needs_rehash(user_record['password']):
            new_hashed_password = password_hasher.hash(user_data['password'])
            change_user_password(user_record['email'], new_hashed_password)

        # According to flask, session just exists? It's to track the user
        # session
        session['email'] = user_record['email']
        session['name'] = user_record['name']
        session['birthday'] = user_record['birthday']

        messages = {
            'message': 'You have successfully logged in!',
            'heading': 'Success',
            'type': 'success'
        }

        return redirect(url_for('app_main', messages=json.dumps(messages)))
    except VerifyMismatchError:
        messages = {
            'message': login_error_message,
            'heading': 'Error',
            'type': 'danger'
        }

        return redirect(url_for('login_register.login_page',
                        messages=json.dumps(messages)))


@login_register.route('/register_main', methods=['POST'])
def perform_register():
    user_data = request.form
    if user_data['password'] != user_data['password_again']:
        message = {
            'message': 'The password do not match!',
            'heading': 'Error',
            'type': 'danger'
        }

        return redirect(url_for('login_register.registration_page',
                        messages=json.dumps(message)))

    # Hash password
    peppered_password = f"{user_data['password']}{SETTINGS['password_pepper']}"
    peppered_pin = f"{user_data['pin']}{SETTINGS['pin_pepper']}"

    password_hasher = PasswordHasher()
    password_hashed = password_hasher.hash(peppered_password)
    pin_hashed = password_hasher.hash(peppered_pin)

    create_user(user_data['name'], user_data['birthday'], user_data['email'],
                password_hashed, pin_hashed)

    message = {
        'message': 'You have been registered! Please login to continue.',
        'heading': 'Success',
        'type': 'success'
    }

    return redirect(url_for('app_main', messages=json.dumps(message)))


@login_register.route('/logout')
def perform_logout():
    if session.get('email'):
        session.pop('email')
        session.pop('name')
        session.pop('birthday')
        messages = {
            'message': 'You have been logged out!',
            'heading': 'Success',
            'type': 'success'
        }

        return redirect(url_for('app_main', messages=json.dumps(messages)))
    else:
        messages = {
            'message': 'You are not logged in!',
            'heading': 'Error',
            'type': 'danger'
        }

        return redirect(url_for('app_main', messages=json.dumps(messages)))


@login_register.route('/login')
@message_capable()
def login_page(**kwargs):
    messages = kwargs.get('messages')
    return render_template('login.html', messages=messages)


@login_register.route('/register')
@message_capable()
def registration_page(**kwargs):
    messages = kwargs.get('messages')
    return render_template('register.html', messages=messages)
