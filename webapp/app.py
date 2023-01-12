from flask import Flask, render_template

app = Flask(__name__)


@app.route("/users/login")
def login_page():
    return render_template('login.html')


@app.route("/users/register")
def registration_page():
    return render_template('register.html')


@app.route("/")
def app_main():
    return 'Hello world!'


if __name__ == '__main__':
    app.run(port=5001)
