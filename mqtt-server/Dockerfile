FROM debian

EXPOSE 1883

EXPOSE 9001

COPY . .

RUN apt update && apt --yes install mosquitto 

RUN mosquitto_passwd -U passfile

RUN cp passfile /etc/mosquitto/passfile

RUN cp mosquitto.conf /etc/mosquitto/mosquitto.conf

RUN /etc/init.d/mosquitto start
