# Задание E5.10

   Деплой django-проекта 'каталог автомобилей' на виртуальную машину (ЯндексОблако)

   ТехЗадание:
   - В качестве домашнего задания вам нужно будет развернуть проект, который вы реализовывали в модуле D10. Соответственно необходимо подключить БД postgreSQL и наполнить её какими-нибудь авто. В качестве ответа нужно скинуть публичный ip-адрес или домен, на котором у вас доступен сервер, а также ссылку на репозиторий с проектом, в котором нужно добавить конфигурации для nginx.

   Деплой django-проекта на виртуальную машину (ЯндексОблако) (только на Linux или MacOS):
1) Сгенерируем ssh-ключ для нашей виртуальной машины (ВМ) с применением придуманного ВМ-пароля:
   - sudo ssh-keygen -t rsa -b 2048
2) Выведем ssh-ключ в окно терминала и скопируем его в буфер:
   - sudo cat ~/.ssh/id_rsa.pub
3) Создадим ВМ на ЯндексОблаке с применением ssh-ключа.
4) Подключаемся к ВМ и вводим ВМ-пароль от сервера:
   - sudo ssh user@ip (где user - имя пользователя и ip - публичный ip-адрес ВМ)
5) Обновляем списки репозиториев и апгрейдимся:
   - sudo apt update
   - sudo apt upgrade
6) Устанавливаем необходимые пакеты:
   - sudo apt install nginx git python3.7 python3-pip libpq-dev python3.7-dev python3.7-venv postgresql postgresql-contrib
7) А терперь, прежде чем настроить nginx, клонируем репозиторий проекта с github.
   - Сгенерируем ssh-ключ для клонирования репозитория:
      - sudo ssh-keygen -t rsa -b 2048
   - Выведем ssh-ключ в окно терминала и скопируем его в буфер:
       - sudo cat ~/.ssh/id_rsa.pub
   - Зарегистрируем на своем аккаунте в разделе "SSH and GPG keys".
8) Клонируем репозиторий проекта с github в /home/user/
   - sudo git clone https://github.com/username/project (где useraname - имя вашего аккаунта и project - название репозитория проекта)
9) После клонирования проекта запускаем nginx:
   - sudo service nginx start
10) Создаем конфигурационный файл nginx для нашего сайта: 
   - sudo nano /etc/nginx/sites-available/project (где project - название нашего проекта)
11) Содержание конфигурационного файла:
server {
    listen 80;
    server_name IP; # где IP - публичный IP нашей ВМ
    location = /favicon.ico { access_log off; log_not_found off; }
    location / {
        proxy_pass http://127.0.0.1:8000;
    }
    location /static/ {
        root /home/user/project/; # путь до папки статических файлов
    }
}
12) Добавляем символическую ссылку конфигурационного файла в папку sites-enabled
   - sudo ln -fs /etc/nginx/sites-available/project /etc/nginx/sites-enabled/
13) Удалим default конфигурационный файл nginx и его ссылку в sites-enabled:
   - sudo rm -f /etc/nginx/sites-enabled/default
   - sudo rm -f /etc/nginx/sites-available/default
14) Проверим наш конфигурационный файл на корректность:
   - sudo nginx -t
   - Должно быть:
      - nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
      - nginx: configuration file /etc/nginx/nginx.conf test is successful
15) Заставляем nginx перечитать конфигурацию:
   - sudo nginx -s reload
16) Но иногда этого может не хватить, тогда мы можем перезапустить nginx полностью:
   - sudo service nginx restart
17) Теперь создадим базу данных (БД) в PostgreSQL:
   - sudo -u postgres psql
18) Выполняем следующие команды:
   - CREATE DATABASE database_name; (где database_name - имя нашей БД)
   - CREATE USER database_user WITH PASSWORD 'database_password'; (где database_user - имя пользователя БД, database_password - пароль для БД)
   - GRANT ALL PRIVILEGES ON DATABASE database_name TO database_user;
   - \q (выход из консоли postgres)
19) Теперь переходим в директорию проекта:
   - cd project
20) Создаем виртуальное окружение:
   - python3.7 -m venv .venv
21) Активируем виртуальное окружение:
   - source .venv/bin/activate
22) Создаем файл виртульного окружения (в той же папке, где находится settings.py)
   - nano project/.env
   - Впишем в него:
      - SECRET_KEY='very_strong_secret_key'
      - DB_NAME='database_name'
      - DB_USER='database_user'
      - DB_PASSWORD='database_password'
      - DB_HOST=127.0.0.1
      - DB_PORT=5432
   - В settings.py: 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv("DB_NAME"),
        'USER': os.getenv("DB_USER"),
        'PASSWORD': os.getenv("DB_PASSWORD"),
        'HOST': os.getenv("DB_HOST", "127.0.0.1"),
        'PORT': os.getenv("DB_PORT", 5432),
    }
}
23) Установим зависимости из файла requirements.txt:
   - pip3 install -r requiremnets.txt
24) Отредактируем settings.py:
   - nano project/settings.py
   - Добавим в него:
      - from dotenv import load_dotenv
      - load_dotenv()
      - DEBUG = False
      - ALLOWED_HOSTS = ['127.0.0.1']
25) Теперь выполняем необходимые команды:
   - python3.7 manage.py collectstatic
   - python3.7 manage.py makemigrations (опционально)
   - python3.7 manage.py migrate
   - python3.7 manage.py createsuperuser
   - python3.7 manage.py loaddata data.json (опционально)
26) По желанию можем запустить сервер командой:
   - python3.7 manage.py runserver
27) Но лучше воспользоваться gunicorn, поэтому устанавливаем его:
   - pip3 install gunicorn
28) Создадим и откроем сокет-файл systemd для Gunicorn:
   - sudo nano /etc/systemd/system/gunicorn.socket
   - Впишем в него следующее:
      - [Unit]
      - Description=gunicorn socket
      - [Socket]
      - ListenStream=/home/user/project/gunicorn.sock
      - [Install]
      - WantedBy=sockets.target
29) Создадим файл конфигурации для gunicorn:
   - sudo nano /etc/systemd/system/gunicorn.service
   - Впишем в него следующее:
      - [Unit]
      - Description=gunicorn daemon
      - Requires=gunicorn.socket
      - After=network.target
      - [Service]
      - User=user
      - Group=www-data
      - WorkingDirectory=/home/user/project/
      - ExecStart=/home/user/project/.venv/bin/gunicorn --access-logfile - --error-logfile error.log --workers 3 --bind unix:/home/user/project/gunicorn.sock project.wsgi:application
      - [Install]
      - WantedBy=multi-user.target
30) Запускаем gunicorn:
   - sudo systemctl start gunicorn
   - sudo systemctl enable gunicorn
   - для проверки: systemctl status gunicorn
31) Редактируем конфигурационный файл nginx:
   - sudo nano /etc/nginx/sites-available/project
   - Вместо:
location / {
    proxy_pass http://127.0.0.1:8000;
}
   - Пропишем:
location / {
    include proxy_params;
    proxy_pass http://unix:/home/user/project/gunicorn.sock;
}
32) Перезапускаем nginx и gunicorn:
   - sudo systemctl restart nginx
   - sudo systemctl restart gunicorn

Данный проект находится на http://84.201.142.198
