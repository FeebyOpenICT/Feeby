FROM node:lts as development

RUN apt-get update \
  && apt-get install git

ENV HOST=0.0.0.0
ENV PORT=3000

WORKDIR /usr/src/app

COPY package*.json ./

RUN npm install

EXPOSE 3000
