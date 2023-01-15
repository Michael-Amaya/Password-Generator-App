import json
from flask import Flask, render_template, request
from flask_session import Session
from login_register import login_register


app = Flask(__name__)

app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = "filesystem"

# Secret key needed for cookie hashing
app.secret_key = '=VMJ@/ZP%7[(.((ZM(*%iu2APbY9w*'

app.register_blueprint(login_register)
Session(app)


@app.route("/")
def app_main():
    messages = request.args.get('messages', None)
    if messages:
        messages = json.loads(messages)
    return render_template('index.html', messages=messages)


if __name__ == '__main__':
    app.run(port=5001)
