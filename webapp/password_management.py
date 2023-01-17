import json
import secrets
from Crypto.Cipher import AES
from flask import Blueprint, render_template, session, redirect, url_for, \
    request
from argon2 import PasswordHasher
from database.database_passwords import get_user_passwords, \
    insert_user_password
from generate_password import generate_password
from utils import login_required, UserDifferenceException, message_capable

password_management = Blueprint('password_management', __name__,
                                template_folder='templates')


@password_management.route('/')
@login_required()
@message_capable()
def password_main(**kwargs):
    messages = kwargs.get('messages')
    return render_template('passwords_main.html', messages=messages)


@password_management.route('/view_passwords')
@login_required()
def view_passwords_main():
    try:
        user_passwords = get_user_passwords(session['email'])
        # print(user_passwords[2]['password'].tobytes())
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
@message_capable()
def create_password_main(**kwargs):
    messages = kwargs.get('messages')
    return render_template('create_password.html', messages=messages)


@password_management.route('/create_password_main', methods=['POST'])
@login_required()
def create_password_logic():
    password_generated = generate_password()
    password_name = request.form.get('pass_alias')
    if not password_name:
        messages = {
            'message': 'There was an error generating your password.',
            'heading': 'Error',
            'type': 'danger'
        }
        return redirect(url_for('password_management.create_password_main',
                                messages=json.dumps(messages)))

    # Process:
    # Generate 32 len token, hash it and get the last 32 chars and encode
    # into bytes. Then use that as the key for AES
    key_part1 = secrets.token_hex(32)
    key_part2 = PasswordHasher().hash(key_part1)[-32:].encode()
    cipher = AES.new(key_part2, AES.MODE_EAX)
    nonce = cipher.nonce
    cipher_text, tag = cipher.encrypt_and_digest(password_generated.encode())

    status = insert_user_password(session['email'], password_name, cipher_text,
                                  key_part2, nonce, tag)
    if not status:
        messages = {
            'message': 'There was an error generating your password.',
            'heading': 'Error',
            'type': 'danger'
        }
        return redirect(url_for('password_management.create_password_main',
                                messages=json.dumps(messages)))

    messages = {
        'message': 'You have successfully created your password!',
        'heading': 'Success',
        'type': 'success'
    }

    return redirect(url_for('password_management.password_main',
                            messages=json.dumps(messages)))
