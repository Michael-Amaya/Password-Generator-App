import json
from functools import wraps
from flask import session, url_for, redirect


def login_required(status=None):
    def login_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if 'email' in session and (status is None or status in session):
                return func(*args, **kwargs)
            else:
                messages = {
                    'message': 'You must be logged in to access that page!',
                    'heading': 'Error',
                    'type': 'danger'
                }

                return redirect(url_for('login_register.login_page',
                                        messages=json.dumps(messages)))
        return wrapper
    return login_decorator


# Exception to be used when getting data from user and another user's data
# is ever detected. There should probably be some logging for this error
# somewhere
class UserDifferenceException(Exception):
    pass
