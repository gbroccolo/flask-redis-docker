FROM tiangolo/uwsgi-nginx:python2.7-alpine3.7

ENV NGINX_MAX_UPLOAD 0
ENV LISTEN_PORT 80
ENV UWSGI_INI /app/uwsgi.ini
ENV STATIC_URL /static
ENV STATIC_PATH /app/static
ENV STATIC_INDEX 0
ENV PYTHONPATH=/app

COPY ./app /app
WORKDIR /app

RUN pip install -r requirements.txt

COPY start.sh /start.sh
RUN chmod +x /start.sh

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

CMD ["/start.sh"]
