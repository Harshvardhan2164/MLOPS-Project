FROM python:3.10-slim-buster

RUN apt update -y && apt install awscli -y
WORKDIR /app

COPY . /app
RUN pip instll -r requirements.txt

CMD ["python", "app.py"]