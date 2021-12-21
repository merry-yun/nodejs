
from django.conf.urls import url
from django.urls import path, re_path, include
from . import views

urlpatterns = [
    # url(r'^$', views.hello),
    # re_path('hello/', views.hello)
    re_path('v1/captcha/pic_verify/', views.pic_verfiry)
]