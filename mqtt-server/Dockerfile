FROM debian

EXPOSE 1883

EXPOSE 9001

COPY . .

RUN apt update && apt --yes install mosquitto

RUN mosquitto_passwd -U password_file

RUN cp password_file mosquitto.conf /etc/mosquitto/
RUN cp password_file mosquitto.conf /etc/mosquitto/conf.d/

CMD mosquitto
