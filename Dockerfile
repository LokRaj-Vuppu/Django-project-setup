FROM python:3.12-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV PATH="/scripts:${PATH}"

# create a directory app in docker and copy app folder contents from local machine to container
RUN mkdir /app
COPY ./app /app
WORKDIR /app
COPY ./requirements.txt .
COPY ./scripts /scripts

RUN chmod +x /scripts/*


RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers


ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN pip install -r requirements.txt

RUN apk del .tmp

# creating static and media files directories
RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static
RUN adduser -D appuser
RUN chown -R appuser:appuser /vol
RUN chmod -R 755 /vol/web

USER appuser

CMD [ "entrypoint.sh" ]