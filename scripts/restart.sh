#!/bin/bash

echo '正在重启服务器'

REMOTE_DIR="/opt/swiper"

PID=`cat $REMOTE_DIR/logs/gunicorn.pid`
kill -HUP $PID

echo '服务器重启完毕'


# 不间断重启
# 主进程: 管理子进程
# 子进程: 接收用户请求

# master 31871

# 旧的子进程，处理完当前请求后会自动关闭

# |- worker(41086) <- 1000
# |- worker(41087) <- 213
# |- worker(41088) <- 582
# |- worker(41089) <- 671

# 先产生一批新的子进程
# |- worker(43062) <- 1042
# |- worker(43059) <- 3221
# |- worker(43058) <- 2334
# |- worker(43057) <- 5299
