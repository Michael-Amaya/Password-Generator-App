import json
from flask import Flask, render_template, request
from login_register import login_register


app = Flask(__name__)
app.register_blueprint(login_register)


@app.route("/")
def app_main():
    messages = json.loads(request.args.get('messages'))
    return render_template('index.html', messages=messages)


if __name__ == '__main__':
    app.run(port=5001)
