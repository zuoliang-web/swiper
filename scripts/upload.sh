#!/bin/bash

LOCAL_DIR="$1"  # 本地项目文件夹
REMOTE_DIR="/opt/swiper"

USER="ubuntu"
HOST="111.229.105.159"

rsync -crvP --exclude={.venv,.git,.vscode,logs,__pycache__} --delete $LOCAL_DIR/ $USER@$HOST:$REMOTE_DIR/

echo -e '文件同步完成\n'

# 在本地重启远程服务器
ssh $USER@$HOST "$REMOTE_DIR/scripts/restart.sh"
