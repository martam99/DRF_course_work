FROM python:3.11

WORKDIR /my_proj

COPY ./requirements.txt /my_proj/

RUN pip install -r /my_proj/requirements.txt

COPY . .
