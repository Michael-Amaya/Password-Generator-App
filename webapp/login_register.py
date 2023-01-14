import secrets
import json
from flask import Blueprint, render_template, request, url_for, redirect
from settings import SETTINGS



login_register = Blueprint('login_register', __name__,
                           template_folder='templates')


@login_register.route('/users/login_main', methods=['POST'])
def perform_login():
    pass


@login_register.route('/users/register_main', methods=['POST'])
def perform_register():
    user_data = request.form
    
    # messages = json.dumps({'message': 'test', 'heading': 'Testing!',
    #                       'type': 'success'})
    # return render_template('index.html', message='test',
    #                        message_header='Testing!',
    #                        message_type='success')
    # return redirect(url_for('app_main', messages=messages))


@login_register.route("/users/login")
def login_page():
    return render_template('login.html')


@login_register.route("/users/register")
def registration_page():
    return render_template('register.html')
