FROM python:3.7-slim

WORKDIR /app_back

COPY requirements.txt /app_back/

RUN pip3 install -r requirements.txt --no-cache-dir

COPY . /app_back/

# CMD ["gunicorn", "backend.wsgi:application", "--bind", "0:8000"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
