import os

import psycopg2
from django.core.management.base import BaseCommand

HOST = os.getenv('DB_HOST')
NAME = os.getenv('DB_NAME')
USER = os.getenv('POSTGRES_USER')
PASSWORD = os.getenv('POSTGRES_PASSWORD')


class Command(BaseCommand):
    help = 'Добавление записей в БД из файлов .csv'
    conn = psycopg2.connect(
        f'host={HOST} dbname={NAME} user={USER} password={PASSWORD}'
    )
    cur = conn.cursor()

    def add_arguments(self, parser):
        parser.add_argument('path', type=str, help='Путь к файлу .csv')
        parser.add_argument(
            'tab_name', type=str, help='Имя таблицы postgresql')

    def handle(self, *args, **kwargs):
        path = kwargs['path']
        table = kwargs['tab_name']
        with open(path, 'r') as f:
            self.cur.copy_from(
                f, table, sep=',', columns=('name', 'measurement_unit')
            )
        self.conn.commit()
