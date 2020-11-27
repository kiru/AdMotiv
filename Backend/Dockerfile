FROM python:3.7.9-slim-stretch
MAINTAINER mstypinski@gmail.com

COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

WORKDIR /app
EXPOSE 8000

