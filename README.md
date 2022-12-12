# English dictionary
Учебный проект, созданный для ознакомления с фреймворком django.

### Инструкция по развертке в тестовой среде

1. Добавления в settings.py настроек

    * SECRET_KEY ...
    * DATABASES ...
    * DEBUG = True
  
2. Устанока django и необходимых пакетов

    * pip install virtualenv
    * virtualenv newenv
    * pip install django==3.0.5
  
3. Миграция базы данных

    * python manage.py makemigrations
    * python manage.py makemigrations english_dict
    * python manage.py migrate
    * python manage.py createsuperuser
  
4. Запуск приложения

    * python manage.py runserver
