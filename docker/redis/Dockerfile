FROM redis:latest

VOLUME /data/redis
COPY ./redis.conf sysctl.conf /etc/
CMD redis-server /etc/redis.conf
