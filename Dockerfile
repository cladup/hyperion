FROM python:3.6-alpine

ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

# Set working directory and copy requirements
WORKDIR /app/src
COPY requirements.txt requirements.txt

# Install application dependencies
RUN apk add --no-cache --virtual .build-deps \
      mariadb-dev build-base musl-dev linux-headers && \
      pip install -r requirements.txt && \
      apk add --virtual .runtime-deps mariadb-client py-mysqldb && \
      apk del .build-deps

COPY . .

EXPOSE 8080

CMD ["python", "api/manage.py", "runserver"]

