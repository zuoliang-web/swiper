#!/bin/bash

REMOTE_DIR="/opt/swiper"

PID=`cat $REMOTE_DIR/logs/gunicorn.pid`
kill $PID
