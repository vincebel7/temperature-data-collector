# Note: There is no Docker support for the collector (client) yet. This is lower priority than the server.
# I was getting an issue that I believe is related to the architecture

#FROM python:3.8-slim-buster
FROM python:3.7.3

MAINTAINER vincebel version: 0.1

ENV TZ=America/Detroit

COPY . .

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN pip install -r requirements.txt

#EXPOSE 8080

CMD ["python3", "collector.py"]
