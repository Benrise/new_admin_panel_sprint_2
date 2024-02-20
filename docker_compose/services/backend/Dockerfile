FROM python:3.10

WORKDIR /opt/app

COPY requirements.txt requirements.txt
COPY uwsgi/uwsgi.ini uwsgi.ini

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

COPY . .

# RUN python manage.py migrate \
#     && python manage.py makesuperuser

EXPOSE 8000

ENTRYPOINT ["uwsgi", "--strict", "--ini", "uwsgi.ini"]