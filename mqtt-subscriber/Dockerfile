#FROM python:3.8-slim-buster
FROM python

MAINTAINER vincebel version: 0.1

ENV TZ=America/Detroit

#WORKDIR /app

#COPY package*.json ./

#RUN npm install

COPY . .

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN pip install -r requirements.txt

#EXPOSE 8080

CMD ["python3", "-u", "subscribe-client.py"]
