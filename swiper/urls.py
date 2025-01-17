"""swiper URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

from user import apis as user_apis
from social import apis as social_apis

urlpatterns = [
    # 用户模块接口
    url(r'^api/user/get_vcode', user_apis.get_vcode),
    url(r'^api/user/submit_vcode', user_apis.submit_vcode),
    url(r'^api/user/get_profile', user_apis.get_profile),
    url(r'^api/user/set_profile', user_apis.set_profile),
    url(r'^api/user/upload_avatar', user_apis.upload_avatar),

    # 社交模块接口
    url(r'api/social/rcmd_users', social_apis.rcmd_users),
    url(r'api/social/like', social_apis.like),
    url(r'api/social/superlike', social_apis.superlike),
    url(r'api/social/dislike', social_apis.dislike),
    url(r'api/social/rewind', social_apis.rewind),
    url(r'api/social/show_who_liked_me', social_apis.show_who_liked_me),
    url(r'api/social/friend_list', social_apis.friend_list),
    url(r'api/social/hot_rank', social_apis.hot_rank),

    # 第三方登录相关接口
    url(r'user/home', user_apis.home),
    url(r'weibo/callback', user_apis.weibo_callback),
    url(r'weibo/callback12', user_apis.weibo_callback22),
]
