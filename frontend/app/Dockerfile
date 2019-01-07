FROM node:10.12-alpine as build-stage
ENV PORT '8080'
WORKDIR /app
COPY . .
RUN yarn install
EXPOSE 8080
ENTRYPOINT ["yarn","serve"]