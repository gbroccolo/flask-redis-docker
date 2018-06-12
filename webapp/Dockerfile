FROM tiangolo/uwsgi-nginx-flask:python2.7-alpine3.7

COPY ./app /app
COPY ./uwsgi_flask_nginx/uwsgi_timeout.conf /etc/nginx/conf.d/
COPY ./uwsgi_flask_nginx/nginx.conf /etc/nginx/
COPY ./uwsgi_flask_nginx/supervisord/rq_worker.ini /etc/supervisor.d/

RUN cd /app &&\
    pip install -r requirements.txt &&\
    rm requirements.txt

WORKDIR /app
