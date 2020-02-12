#!/bin/bash

REMOTE_DIR="/opt/swiper"

cd $REMOTE_DIR
source .venv/bin/activate
gunicorn -c $REMOTE_DIR/swiper/gconfig.py swiper.wsgi
deactivate
cd -
