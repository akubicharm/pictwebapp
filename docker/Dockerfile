FROM python:3-stretch

WORKDIR /app

COPY app.py .
COPY requirements.txt .
COPY templates/ templates/

RUN python3 -m venv venv

RUN . ./venv/bin/activate

RUN pip install -r ./requirements.txt
RUN pip install flask

ENV FLASK_APP app.py
CMD flask run -h 0.0.0.0 -p 80