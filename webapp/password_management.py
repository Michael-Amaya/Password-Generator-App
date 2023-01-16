from flask import Blueprint, render_template
from utils import login_required

password_management = Blueprint('password_management', __name__,
                                template_folder='templates')


@password_management.route('/passwords')
@login_required()
def password_main():
    return render_template('passwords_main.html')
