#!/bin/bash

REMOTE_DIR="/opt/swiper"
mkdir -p $REMOTE_DIR/logs
export SWIPER_DOCKER=1
export C_FORCE_ROOT=1

cd $REMOTE_DIR
celery worker -A tasks --loglevel=info
