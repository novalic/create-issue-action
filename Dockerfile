FROM python:3.10.7-buster

COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY app /app

CMD ["python", "/app/app.py"]
