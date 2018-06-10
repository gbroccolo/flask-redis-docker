FROM tiangolo/uwsgi-nginx:python2.7-alpine3.7

COPY ./app /app

RUN cd /app && pip install -r requirements.txt && cd -
