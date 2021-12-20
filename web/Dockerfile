FROM node:10.19.0

MAINTAINER vincebel version: 0.1

ENV TZ=America/Detroit

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

EXPOSE 8080

CMD ["node", "app.js"]
