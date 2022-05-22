# praktikum_new_diplom

Readme будет дописано после первого этапа ревьью.

## Описание

В настоящий момент проект запускается локально в трех контейнерах.

Для запуска:

1. Создайте файл .env в директории infra с содержимым:
```
SECRET_KEY=<КЛЮЧ>
DB_ENGINE=django.db.backends.postgresql
DB_NAME=<ИМЯ БАЗЫ ДАННЫХ>
POSTGRES_USER=<ИМЯ ЮЗЕРА БД>
POSTGRES_PASSWORD=<ПАРОЛЬ БД>
DB_HOST=db
DB_PORT=5432
```

2. В папке infra следует выполнить команды:
```
docker-compose up -d
docker-compose exec backend python manage.py makemigrations
docker-compose exec backend python manage.py migrate (может потребоваться указать --fake)
docker-compose exec backend python manage.py collectstatic --no-input
```

3. Для создания суперпользователя, выполните команду:
```
docker-compose exec backend python manage.py createsuperuser
```

4. Для добавления ингредиентов в базу данных, выполните команду:
```
docker-compose exec backend python manage.py add_data ingredients.csv tags_ingr_ingredient
```

Проект запущен на адресе: http://localhost/
API проекта: http://localhost/api/
Admin-зона: http://localhost/admin/
