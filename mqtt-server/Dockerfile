FROM debian

EXPOSE 1883

EXPOSE 9001

COPY . .

RUN apt-get update && apt-get --yes install mosquitto

RUN mkdir /var/run/mosquitto && chown mosquitto: /var/run/mosquitto

RUN mosquitto_passwd -U password_file

RUN cp password_file mosquitto.conf /etc/mosquitto/conf.d/

CMD mosquitto -c /etc/mosquitto/conf.d/mosquitto.conf
