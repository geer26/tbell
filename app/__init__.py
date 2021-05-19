from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_restful import Api
from config import SQLite
from flask_socketio import SocketIO


app = Flask(__name__)
app.config.from_object(SQLite)

'''
dbtype = os.environ.get('DB_TYPE')
if not dbtype or dbtype == 'SQLite':
    app.config.from_object(SQLite)
elif dbtype and dbtype == 'PostgreSQL':
    app.config.from_object(PostgreSQL)
'''

'''
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)
'''

login = LoginManager(app)

'''
db = SQLAlchemy(app)
migrate = Migrate(app, db)

with app.app_context():
    if db.engine.url.drivername == 'sqlite':
        migrate.init_app(app, db, render_as_batch=True)
    else:
        migrate.init_app(app, db)
'''

socket = SocketIO(app)
socket.init_app(app, cors_allowed_origins="*")


db = SQLAlchemy(app)
migrate = Migrate(app, db)
migrate.init_app(app, db, render_as_batch=True)

api = Api(app)

valid_apikeys = []

from app import routes, models, restful