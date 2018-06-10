FROM python:2.7.15-alpine3.6

COPY ./app /app
WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "worker.py"]
