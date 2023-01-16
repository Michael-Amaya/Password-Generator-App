import os
import sys
import psycopg2

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from settings import SETTINGS


CONNECTION = psycopg2.connect(database=SETTINGS['database_name'],
                              host=SETTINGS['database_host'],
                              user=SETTINGS['database_user'],
                              password=SETTINGS['database_password'],
                              port=SETTINGS['database_port'])

CURSOR = CONNECTION.cursor()
