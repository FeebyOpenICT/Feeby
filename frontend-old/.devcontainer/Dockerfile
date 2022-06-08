FROM mcr.microsoft.com/vscode/devcontainers/javascript-node:dev-16-bullseye as development

RUN apt-get update \
  && apt-get install git

ENV HOST=0.0.0.0
ENV PORT=3000

WORKDIR /usr/src/app

COPY package*.json ./

RUN yarn

EXPOSE 3000

