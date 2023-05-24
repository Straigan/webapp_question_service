from flask import Flask
from flask_migrate import Migrate

from webapp.db import db
from webapp.question_service.views import blueprint as question_service_blueprint
from webapp.question_service.models import Question_answer


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    Migrate(app, db)
    app.register_blueprint(question_service_blueprint)
    with app.app_context():
        db.create_all()

    return app
