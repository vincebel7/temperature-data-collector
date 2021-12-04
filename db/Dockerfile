FROM ubuntu

RUN apt-get update && apt-get install -y mysql-server

EXPOSE 3306

#RUN apt-get update && apt-get install -y mariadb-server

ADD sensordump.sql /docker-entrypoint-initdb.d

ENTRYPOINT service mysql start && /bin/bash

CMD ["mysql", "-u", "root", "-psup3r_secur3_pw"]
