import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

POSTGRESQL = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'database', #database name
        'USER': 'postgres',
        'PASSWORD': '76543210', #password in file .env
        'HOST': 'localhost',
        'PORT': '5432'
    }
}
