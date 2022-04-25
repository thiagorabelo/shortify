FROM python:3.9.12-alpine

RUN mkdir -p /shortify \
    && addgroup -S shortify \
    && adduser -S -D -H -G shortify -g "Shortify User" shortify

COPY . /shortify/

WORKDIR /shortify

RUN pip install $(grep -v 'pywatchman' requirements.txt | grep .) \
    && chmod +x bin/gunicorn_start.sh

USER shortify

CMD [ "bin/gunicorn_start.sh" ]
