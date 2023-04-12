FROM python:3.8.2

SHELL ["/bin/bash", "-c"]

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

WORKDIR /application

RUN pip install -r requirements.txt

CMD ["manage.py runserver"]