from flask import Blueprint, jsonify, request
from sqlalchemy import func

from webapp.db import db
from webapp.question_service.models import Question_answer
from webapp.services.jservice_service import process_check_to_valid_and_save_questions


blueprint = Blueprint('question_service',  __name__)

@blueprint.route('/api/v1.0', methods=['POST'])
def post_questions_num() -> dict:
    """Сервис на вход принимает запросы с содержимым вида {"questions_num": integer}"""

    data_questions_num = request.json['questions_num']
    process_check_to_valid_and_save_questions(data_questions_num)
    
    last_record_db = Question_answer.query.order_by(Question_answer.id.desc()).first()

    """При отсутсвии вопросов в БД, отправлятся пустой объект"""
    if last_record_db == None:
        return {}
    else:  
        last_record_json = jsonify(
            id = last_record_db.id, 
            id_question = last_record_db.id_question, 
            text_question = last_record_db.text_question, 
            text_answer = last_record_db.text_answer, 
            creation_datetime = last_record_db.creation_datetime
            )
        
        return last_record_json
