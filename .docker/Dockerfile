FROM python:3.8.2

SHELL ["/bin/bash", "-c"]

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

ADD . /application/
WORKDIR /application


RUN pip3 install --no-cache-dir -r /application/requirements.txt


CMD ["manage.py runserver"]