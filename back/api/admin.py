from django.contrib import admin
from .models import *

class HotelAdmin(admin.ModelAdmin):
    model = Hotel
    list_display = ['name', 'address', 'description', ]
admin.site.register(Hotel,HotelAdmin)
admin.site.register(HotelImages)
admin.site.register(Rooms)
admin.site.register(Orders)
admin.site.register(Meals)
