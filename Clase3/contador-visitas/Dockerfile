FROM python:alpine3.16

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]