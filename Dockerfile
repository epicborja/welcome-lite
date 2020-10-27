FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


ARG GECKODRIVER_VERSION=0.27.0

WORKDIR /welcome

COPY Pipfile Pipfile.lock /welcome/
RUN pip install pipenv && pipenv install --system

COPY . /welcome/

CMD gunicorn welcome_lite.wsgi --bind 0.0.0.0:8000 --reload



