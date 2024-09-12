from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),  # 直接使用空字符串匹配根路径
]