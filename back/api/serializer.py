from .models import * 
from rest_framework import serializers


class HotelSerializer(serializers.ModelSerializer):
    # yuotube_change = serializers.CharField(source='video_change', read_only=True)
    # date_time = serializers.CharField(source='time', read_only=True)
    class Meta():
        model = Hotel
        fields = ('pk','name','address','img','description','created','phone')

class HotelVipSerializer(serializers.ModelSerializer):
    class Meta():
        model = Hotel
        fields = ('pk','name','address','img','phone')

class OrderSerializer(serializers.ModelSerializer):
    class Meta():
        model = Orders
        fields = ('author','address','hotel','room_id','phone','description','add_date','back_date')

class RoomSerializer(serializers.ModelSerializer):
    class Meta():
        model = Rooms
        fields = ('name','hotel','price','address','bath','sport','bar','car','wifi','img','description')

class MealsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meals
        fields = ('name','category','hotel','img','created','description')

