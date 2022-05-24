# Foodgram React

![foodgram_workflow](https://github.com/AbbadonAA/foodgram-project-react/workflows/foodgram_workflow/badge.svg)

## Описание

Сервис для публикации рецептов и формирования списка покупок.

## Доступ

Проект запущен на сервере YCloud и доступен по адресам:
- http://abbadon.zapto.org
- http://51.250.109.189/
- Админ-зона: http://abbadon.zapto.org/admin/
  - username: admin
  - password: foodgram_admin
- API: http://abbadon.zapto.org/api/

## Для запуска на собственном сервере:

1. На сервере создайте директорию infra и поместите в неё файлы .env, docker-compose.yml и nginx.conf

2. Файл .env должен быть заполнен следующими данными:
```
SECRET_KEY=<КЛЮЧ>
DB_ENGINE=django.db.backends.postgresql
DB_NAME=<ИМЯ БАЗЫ ДАННЫХ>
POSTGRES_USER=<ИМЯ ЮЗЕРА БД>
POSTGRES_PASSWORD=<ПАРОЛЬ БД>
DB_HOST=db
DB_PORT=5432
```

3. В директории infra следует выполнить команды:
```
docker-compose up -d
docker-compose exec backend python manage.py makemigrations
docker-compose exec backend python manage.py migrate (может потребоваться указать --fake)
docker-compose exec backend python manage.py collectstatic --no-input
```

4. Для создания суперпользователя, выполните команду:
```
docker-compose exec backend python manage.py createsuperuser
```

5. Для добавления ингредиентов в базу данных, выполните команду:
```
docker-compose exec backend python manage.py add_data ingredients.csv tags_ingr_ingredient
```
После выполнения этих дейстий проект будет запущен в трех контейнерах (backend, db, nginx) и доступен по адресам:

http://<ip-адрес>/

API проекта: http://<ip-адрес>/api/

Admin-зона: http://<ip-адрес>/admin/
