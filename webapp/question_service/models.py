from datetime import datetime

from webapp.db import db


class Question_answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_question = db.Column(db.Integer, unique=True)
    text_question = db.Column(db.String)
    text_answer = db.Column(db.String)
    creation_datetime = db.Column(db.DateTime, default=datetime.now())

    def __repr__(self):
        return f'<Question: {self.id_question}, id: {self.id}, text_question: {self.text_question}>'
