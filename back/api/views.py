# from django.shortcuts import render
from rest_framework import generics,filters
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from .models import *
from .serializer import *


class HotelList(generics.ListCreateAPIView):
    search_fields =['name']
    filter_backends = [filters.SearchFilter]
    filterset_fields = ['name']
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    name = 'hotel-list'


class HotelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    name = 'hotel-detail'

class RoomList(generics.ListCreateAPIView):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['hotel']
    queryset = Rooms.objects.all()
    serializer_class = RoomSerializer
    name = 'room-list'

class RoomDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rooms.objects.all()
    serializer_class = RoomSerializer
    name = 'room-detail'

class MealsList(generics.ListCreateAPIView):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['hotel']
    queryset = Meals.objects.all()
    serializer_class = MealsSerializer
    name = 'meals-list'


class MealsDetail(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Meals.objects.all()
    serializer_class = MealsSerializer
    name = 'meals-detail'

class VipList(generics.ListCreateAPIView):
    queryset = Hotel.objects.filter(vip=True)
    serializer_class = HotelVipSerializer
    name = 'vip-list'


class VipDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hotel.objects.filter(vip=True)
    serializer_class = HotelVipSerializer
    name = 'vip-detail'

@api_view(['POST'])
def create_order(request):
    if request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = OrderSerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    else:
        return JsonResponse({'message': 'Maglumaty goşmak ýerine ýetmedi!'})

class ApiRoot(generics.GenericAPIView):
    name = 'alem'

    def get(self, request, *args, **kwargs):
        return Response({
            '1-hotels': reverse(HotelList.name, request=request),
            '2-rooms': reverse(RoomList.name, request=request),
            '3-meals': reverse(MealsList.name, request=request),
            '4-vip': reverse(VipList.name, request=request),
            })