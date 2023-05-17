from flask import Flask
from flask_migrate import Migrate

from webapp.db import db
from webapp.question_service.views import blueprint as question_service_blueprint


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    migrate = Migrate(app, db)
    app.register_blueprint(question_service_blueprint)

    return app
