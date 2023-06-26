FROM python:3.10
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY . /app
RUN apt update && apt install pipenv
RUN pipenv install --system --deploy 

CMD python manage.py runserver 0.0.0.0:8000