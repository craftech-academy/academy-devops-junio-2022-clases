FROM alpine

ENV BRANCH=main

ENV PYTHONUNBUFFERED=1

RUN apk add --no-cache python3 py3-pip

COPY script.py .

CMD ["python3", "script.py"]
