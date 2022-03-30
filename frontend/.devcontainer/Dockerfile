FROM node:lts as development

RUN adduser --uid 5678 --disabled-password --gecos "" vscode

RUN apt-get update \
  && apt-get install git

ENV HOST=0.0.0.0
ENV PORT=3000

WORKDIR /usr/src/app

COPY package*.json ./

RUN yarn

EXPOSE 3000

