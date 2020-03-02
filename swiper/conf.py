'''程序逻辑和第三方平台的配置'''
import os

SWIPE_SCORE = {
    'like': 5,
    'superlike': 7,
    'dislike': -5,
}


# Redis 配置
REDIS = {
    'host': '172.18.0.20' if 'SWIPER_DOCKER' in os.environ else 'localhost',
    'port': 6379,
    'db': 6,
}


# 云之讯短信平台配置
YZX_SMS_API = 'https://open.ucpaas.com/ol/sms/sendsms'
YZX_SMS_ARGS = {
    "sid": '4ad2912058ef9ef9ea0cdd790e0f7361',
    "token": 'cc2de93f90e7356abf9580a7de00074b',
    "appid": '3a34537ffb294f0a8af45555a161e68a',
    "templateid": '527103',
    "param": None,
    "mobile": None
}


# 七牛云配置
QN_ACCESSKEY = "kEM0sRR-meB92XU43_a6xZqhiyyTuu5yreGCbFtw"
QN_SECRETKEY = "QxTKqgnOb_UVldphU261qu9IdzmjkgGHh6GQVPPy"
QN_BUCKET = 'sh1906'
QN_BASE_URL = 'http://q3oh1b1oq.bkt.clouddn.com'


# 微博登陆配置
WB_APP_KEY = "415847342"
WB_APP_SECRET = "25bb6f5efd2f2d69177095562f031e3b"
WB_CALLBACK = "http://127.0.0.1:8000/weibo/callback"
WB_AUTH_API = "https://api.weibo.com/oauth2/authorize"
WB_ACCESS_TOKEN_API = 'https://api.weibo.com/oauth2/access_token'
WB_USERS_SHOW = 'https://api.weibo.com/2/users/show.json'
