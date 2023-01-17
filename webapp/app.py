import json
from flask import Flask, render_template, request
from flask_session import Session
from utils import message_capable

# Webpage import
from login_register import login_register
from password_management import password_management


app = Flask(__name__)

app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = "filesystem"

# Secret key needed for cookie hashing
app.secret_key = '=VMJ@/ZP%7[(.((ZM(*%iu2APbY9w*'

app.register_blueprint(login_register, url_prefix='/users')
app.register_blueprint(password_management, url_prefix='/passwords')
Session(app)


@app.route("/")
@message_capable()
def app_main(**kwargs):
    messages = kwargs.get('messages')
    return render_template('index.html', messages=messages)


if __name__ == '__main__':
    app.run(port=5001)
