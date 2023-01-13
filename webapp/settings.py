import json


SETTINGS = None


if SETTINGS is None:
    print("Setting up settings..")
    try:
        with open('settings.json', encoding='UTF-8') as settings_file:
            SETTINGS = json.load(settings_file)
    except Exception:
        # Default config
        SETTINGS = {
            'database_host': 'localhost',
            'database_port': 5432,
            'database_name': 'pwd_test',
            'database_user': 'myuser',
            'database_password': 'password',
            # Password pepper is randomly generated
            'password_pepper': 'N[h@8q$GLeU3r=;cVw2CSRX(pSwFmm',
        }
