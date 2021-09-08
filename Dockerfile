# syntax=docker/dockerfile:1
FROM python:3.8.5
WORKDIR /app
COPY requirements.txt /app/
RUN pip3 install -r requirements.txt
COPY . .
CMD [ "python","main.py" ]
