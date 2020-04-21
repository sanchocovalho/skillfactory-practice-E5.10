# Задание D5.11

   Проект домашней библиотеки. Функционал включает следующие моменты:

  - Через панель администратора: возможно добавление, изменение и удаление книг, авторов, друзей, издательств;
  - Без администратора возможно добавление и изменение книг, авторов, друзей, изданий.

   ТехЗадание:
  - Сейчас наша библиотека отражает, какие книги у нас есть. Что, если ваш друг попросит у вас что-то почитать? Для того чтобы не запутаться и всегда помнить, кому и какую книгу вы отдали, давайте модифицируем наш проект.
  - Нам нужно добавить модель "Друга" и описать для неё необходимые поля. Знания о полях можно освежить в документации.
  - Кроме этого, вероятно, потребуется внести изменения в уже существующие модели, чтобы отразить отношения моделей "Книга" и "Друг". Мы должны понимать, какие книги были одолжены, кому они были одолжены.
  - Добавьте несколько записей в таблицу друзей для того, чтобы можно было легко проверить работу приложения.

Для того, чтобы запустить локальный сервер необходимо:
1) Распакуйте проект в папку и через терминал зайдите в директорию проекта
2) Создате виртуальное окружение:
   - python -m venv django
3) Активируйте виртуальное окружение:
   - django\Scripts\activate.bat
4) Установите все необходимые пакеты:
   - pip install -r requirements.txt
5) Выпонить следующие команды:
   - python manage.py makemigrations
   - python manage.py migrate
   - python manage.py loaddata data.xml
   - python manage.py runserver

Для того, чтобы сделать деплой на heroku необходимо (при Debug=False):
1) Изменить в settings.py:
   - SECRET_KEY = 'Ваш_секретный_код' на SECRET_KEY = os.environ.get('SECRET_KEY')
   - ALLOWED_HOSTS = ['название_домена_проекта_на_heroku'] (например, ['mylibrary-skillfactory.herokuapp.com']
   - DATABASES = {'default': {'ENGINE': 'django.db.backends.sqlite3','NAME': os.path.join(BASE_DIR, 'db.sqlite3'),}} на import dj_database_url и DATABASES = {'default': dj_database_url.config(default=os.environ['DATABASE_URL'])}
2) Перейти в каталог с проектом (например):
   - cd C:\my_site
3) Если используете статические файлы, то обязательно в проекте должны быть созданы две папки: static и staticfiles
4) Выполнить следующий команды:
   - git init
   - git add .
   - git commit -m "initial commit
   - heroku login
   - heroku create
   - heroku rename -a oldname newname (переименовываем приложение, если необходимо)
   - heroku addons:create heroku-postgresql --as DATABASE
   - heroku config:set SECRET_KEY=Ваш_секретный_код
   - git push heroku master
   - heroku run python manage.py makemigrations
   - heroku run python manage.py migrate
   - heroku run python manage.py loaddata data.xml
   - heroku run python manage.py createsuperuser
5) Запускаем приложение:
   - heroku open

   Данный проект находится на https://mylibrary-skillfactory.herokuapp.com/
