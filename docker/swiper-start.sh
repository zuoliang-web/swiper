#!/bin/bash

REMOTE_DIR="/opt/swiper"
mkdir -p $REMOTE_DIR/logs
export SWIPER_DOCKER=1

cd $REMOTE_DIR
gunicorn -c $REMOTE_DIR/swiper/gconfig_docker.py swiper.wsgi
