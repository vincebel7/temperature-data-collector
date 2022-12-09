FROM debian

EXPOSE 1883

EXPOSE 9001

COPY . .

RUN apt-get update && apt-get --yes install mosquitto

RUN mkdir /var/run/mosquitto && chown mosquitto: /var/run/mosquitto

COPY entrypoint.sh /entrypoint.sh

#ENTRYPOINT ["sh", "/entrypoint.sh"]

RUN mosquitto_passwd -U password_file

RUN cp password_file mosquitto.conf /etc/mosquitto/conf.d/

#RUN cat /etc/mosquitto/conf.d/password_file

CMD mosquitto -c /etc/mosquitto/conf.d/mosquitto.conf
