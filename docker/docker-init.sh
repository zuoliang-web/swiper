#!/bin/bash

# 创建容器网络 和 存储卷
docker network create --subnet=172.18.0.0/16 swiper-net
docker volume create swiper-rds
docker volume create swiper-db

# 启动 Redis 容器
docker run -d \
           --name=rds \
           -v swiper-rds:/data/redis \
           --network=swiper-net \
           --ip=172.18.0.20 \
           rds:latest

# 启动 MySQL 容器
docker run -d \
           --name=db \
           -v swiper-db:/var/lib/mysql \
           --network=swiper-net \
           --ip=172.18.0.30 \
           -e MYSQL_ROOT_PASSWORD=123 \
           mysql:5.7.29

# 启动 Swiper 容器
docker run -d \
           --name=web \
           -v /opt/swiper:/opt/swiper \
           --network=swiper-net \
           --ip=172.18.0.10 \
           -p 9000:9000 \
           -e SWIPER_DOCKER=1 \
           swiper:latest

# 启动 Celery 容器
docker run -d \
           -v /opt/swiper:/opt/swiper \
           --name=celery \
           -v /opt/swiper:/opt/swiper \
           --network=swiper-net \
           --ip=172.18.0.40 \
           -e SWIPER_DOCKER=1 \
           swiper:latest bash /opt/swiper/docker/celery-start.sh
