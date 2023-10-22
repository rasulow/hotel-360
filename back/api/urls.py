from django.contrib import admin
# from .views_serializers import *
# from django.conf.urls import url
from django.urls import path, include,re_path
from .views import *

urlpatterns = [
    # path('hotel/', main, name='mains'),
    re_path(r'^create-order/$', create_order, name='create-order'),
    re_path(r'^hotel-list/$', HotelList.as_view(), name=HotelList.name),
    re_path(r'^hotel-detail/(?P<pk>[0-9]+)$', HotelDetail.as_view(), name=HotelDetail.name),
    re_path(r'^vip-list/$', VipList.as_view(), name=VipList.name),
    re_path(r'^vip-detail/(?P<pk>[0-9]+)$', VipDetail.as_view(), name=VipDetail.name),
    re_path(r'^room-list/$', RoomList.as_view(), name=RoomList.name),
    re_path(r'^room-detail/(?P<pk>[0-9]+)$', RoomDetail.as_view(), name=RoomDetail.name),
    re_path(r'^meals-list/$', MealsList.as_view(), name=MealsList.name),
    re_path(r'^meals-detail/(?P<pk>[0-9]+)$', MealsDetail.as_view(), name=MealsDetail.name),
    re_path(r'^$', ApiRoot.as_view(), name=ApiRoot.name)
]
