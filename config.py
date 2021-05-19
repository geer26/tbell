import os
from os import environ, path
from dotenv import load_dotenv


basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

""" CONFIGS """
class Config:
    """Base config."""
    SECRET_KEY = environ.get('SECRET_KEY') or '01!ChAnGeThIs!10'
    SESSION_COOKIE_NAME = environ.get('SESSION_COOKIE_NAME') or '!Tbell2021!'
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'

    COOKIE_LIFESPAN = 60*60*24*30

    """
    MAIL_SERVER = environ.get('MAIL_SERVER') or 'mail.tesztelgeto.tk'
    #MAIL_USERNAME = environ.get('MAIL_USERNAME') or None
    MAIL_USERNAME = None
    #MAIL_PASSWORD = environ.get('MAIL_PASSWORD') or None
    MAIL_PASSWORD = None
    MAIL_DEFAULT_SENDER = environ.get('MAIL_DEFAULT_SENDER') or None
    MAIL_PORT = environ.get('MAIL_PORT') or 25
    MAIL_USE_TLS = environ.get('MAIL_USE_TLS') or True

    TEMPLATES_AUTO_RELOAD = True

    UPLOAD_FOLDER = path.join(basedir, 'app/uploads/')

    BACKUP_FOLDER = path.join(basedir, 'app/backup/')

    LOG_FOLDER = path.join(basedir, 'app/log/')

    #CLIENT_LISTS = path.join('app/temp/')
    ALLOWED_EXTENSIONS = {'zip'}
    #SENDGRID_API_KEY = environ.get('SENDGRID_API_KEY') or 'APIKEY'
    #LANG = environ.get('LANG') or 'C.UTF-8'
    #LC_ALL = environ.get('LC_ALL') or 'C.UTF-8'"""

class PostgreSQL(Config):
    """Production config."""
    """FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = environ.get('POSTGRES_URI')"""


class SQLite(Config):
    """Development config."""
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
    DATABASE_URI = environ.get('DEV_DATABASE_URI')
    SQLALCHEMY_DATABASE_URI = environ.get('SQLITE_URI') or \
                              'sqlite:///' + path.join(basedir, 'data.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False