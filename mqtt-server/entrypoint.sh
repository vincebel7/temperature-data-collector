#!/bin/sh

PASSWDFILE=password_file

if [ -f $PASSWDFILE ]; then
	echo "Loading MQTT passwords to server"
	#mosquitto_passwd -b $PASSWDFILE $MQTT_PUB_USER $MQTT_PUB_PASS
	#mosquitto_passwd -b $PASSWDFILE $MQTT_SUB_USER $MQTT_SUB_PASS
	echo "$MQTT_SUB_USER:$MQTT_SUB_PASS" > $PASSWDFILE
	echo "$MQTT_PUB_USER:$MQTT_PUB_PASS" >> $PASSWDFILE
	#cat $PASSWDFILE
	#mosquitto_passwd -U $PASSWDFILE
fi

exec "$@"
