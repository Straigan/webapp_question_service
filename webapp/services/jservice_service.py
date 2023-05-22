from requests import get

from webapp.db import db
from webapp.question_service.models import Question_answer


def get_question_jservice(questions_quantity: int=1) -> dict:
    """ 
        После получения колличества запрашиваемых вопросов сервис, в свою очередь, 
        запрашивает с публичного API (англоязычные вопросы для викторин) 
        https://jservice.io/api/random?count=1 указанное в полученном запросе количество вопросов.
    """
    address_questions_jservice = f'https://jservice.io/api/random?count={questions_quantity}'

    questions_in_jservice = get(address_questions_jservice).json()

    return questions_in_jservice


def save_question_in_db(question: dict) -> None:
    """Сохранение данных вопроса в базу данных"""

    add_question = Question_answer(
        id_question = question['id'],
        text_question = question['question'],
        text_answer = question['answer'],
        )
    
    db.session.add(add_question)
    db.session.commit()
    

def process_check_to_valid_and_save_questions(data_questions_num: int) -> None:
    try:
        questions_in_jservice = get_question_jservice(data_questions_num)
    except:
        return print('Сайт jservice.io не доступен')
    for question in questions_in_jservice:
        """
            Если в БД имеется такой же вопрос, к публичному API с викторинами выполняются дополнительные запросы до тех пор
            пока не будет получен уникальный вопрос для викторины.
        """

        questions_in_db = Question_answer.query.filter_by(id_question=question['id']).first()
    
        if questions_in_db != None:
            questions_in_jservice.append(get_question_jservice())
        
        else:
            save_question_in_db(question)
