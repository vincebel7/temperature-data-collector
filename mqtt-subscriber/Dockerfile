FROM python

MAINTAINER vincebel version: 0.1

ENV TZ=America/Detroit

COPY . .

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN pip install -r requirements.txt

CMD ["python3", "-u", "subscribe-client.py"]
