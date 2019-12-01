FROM python:3.7.5

LABEL maintainer "jaime.viloria@@gmail.com"

RUN mkdir -p app
COPY ./app/ ./app/
WORKDIR ./app
RUN pip3 install --no-cache-dir -r ./requirements/requirements.txt
RUN python manage.py migrate

EXPOSE 8080

CMD ["python","manage.py","runserver","0.0.0.0:8080"]
