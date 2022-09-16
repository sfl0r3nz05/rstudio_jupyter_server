FROM nginx:1.19.4

COPY nginx.conf /etc/nginx/nginx.conf
COPY certs /certs

RUN mkdir -p /etc/nginx/logs/ && touch /etc/nginx/logs/access.log