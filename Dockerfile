FROM python:3.8-alpine

WORKDIR /usr/alcobot

EXPOSE 18801

ENV TZ=Europe/Moscow

RUN apk add --no-cache tzdata

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/*.py ./src/

CMD ["python3", "-B", "src/main.py"]