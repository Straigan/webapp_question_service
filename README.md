# Webapp question service

##  Webapp question service - это web-приложение на Flask.

При разработке приложения применялись технлогии: Flask, PostgreSql, SQLAalchemy, docker-compose.  
В сервисе реализован POST REST метод, принимающий на вход запросы с содержимым вида {"questions_num": integer}, далее происходит запрос вопросов у публичного API https://jservice.io/api/random?count=1  c указанным в полученном запросе количеством вопросов. Далее происходит проверка полученных вопросов, если вопрос есть в базе данных, тогда проиходит повторный запрос на публичный API, если такого вопроса нет, то вопрос сохраняется в базу данных.  

# Сборка репозитория и запуск

## Настройка

Выполните в консоли:

git clone https://github.com/Straigan/webapp_question_service.git

Необходимо создать файл .env и присвоить значения следующим переменным  

Пример файла .env:  
FLASK_APP='webapp'  
DATABASE_URL='postgresql://flaskuser:flaskpassword@postgres:5432/flaskdb'  
SECRET_KEY='weq1312eqwe'

Данные для формирования подключения к БД в docker, указываются в 'docker/.env-postgresql'.  

Пример файла .env-postgresql:  
DATABASE_PORT=5432  
DATABASE_DIALECT=postgresql  
POSTGRES_DB=flaskdb  
POSTGRES_USER=flaskuser  
POSTGRES_PASSWORD=flaskpassword  

## Запуск приложения на ОС Linux:

Находясь в корневой директории проекта, введите в консоли:  
docker-compose up  

Для отправки запроса с запрашиваемым колличеством вопросов, введите в консоли:  
curl -i -H "Content-Type: application/json" -X POST -d '{"questions_num": 2}' http://localhost:5000/api/v1.0  
В запросе укажите запрашиваемое кол-во вопрсово: {"questions_num": 2}.