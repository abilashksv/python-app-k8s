FROM python:3

ADD . /flask-api

RUN pip install -r /flask-api/requirements.txt

CMD [ "python", "/flask-api/run_app.py" ]
