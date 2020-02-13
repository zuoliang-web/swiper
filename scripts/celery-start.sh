#!/bin/bash

REMOTE_DIR="/opt/swiper"

cd $REMOTE_DIR
source .venv/bin/activate
nohup celery worker -A tasks --loglevel=info &
deactivate
cd -
