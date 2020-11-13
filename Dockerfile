FROM python:3.7-alpine

WORKDIR /code

ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0

RUN apk add --no-cache gcc musl-dev linux-headers

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app.py .

EXPOSE 5000
USER 1000

CMD ["flask", "run"]