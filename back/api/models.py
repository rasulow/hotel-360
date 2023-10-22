from django.db import models

class HotelImages(models.Model):
    name = models.CharField(max_length=255,  null=True)
    img = models.ImageField(upload_to='hotel_images')
    hotel = models.ForeignKey("Hotel", on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Surat'
        verbose_name_plural = 'Suratlar'

    def __str__(self):
        return self.name

class Orders(models.Model):
    author = models.CharField(max_length=255,  null=True,verbose_name='Sargyt eden')
    address = models.CharField(max_length=255,  null=True,verbose_name='Salgysy')
    hotel = models.ForeignKey("Hotel", on_delete=models.CASCADE,verbose_name='Myhmanhana')
    room_id = models.ForeignKey("Rooms", on_delete=models.CASCADE,verbose_name='Otagy')
    phone = models.CharField(max_length=11,null=True)
    description = models.TextField(null=True,verbose_name='Maglumaty')
    add_date = models.DateField(verbose_name='Sargyt edilmeli wagty')
    back_date = models.DateField(verbose_name='Sargyt edilmeli wagty',null=True)
    created = models.DateField(auto_now_add=True)
    checked = models.BooleanField(default=True,verbose_name='Kabul edildi')

    class Meta:
        verbose_name = 'Sargyt'
        verbose_name_plural = 'Sargytlar'

    def __str__(self):
        return self.author

class Hotel(models.Model):
    name = models.CharField(max_length=255,  null=True,verbose_name='Ady')
    address = models.CharField(max_length=255,  null=True,verbose_name='Salgysy')
    web_url = models.CharField(max_length=255,  null=True,verbose_name='Web salgysy')
    img = models.ImageField(upload_to='hotel_images',null=True,verbose_name='Suraty')
    phone = models.CharField(max_length=11,null=True,verbose_name='Telefon belgisi')
    description = models.TextField(null=True,verbose_name='Maglumaty')
    created = models.DateField(auto_now_add=True)
    vip = models.BooleanField(default=True,verbose_name='Vip otag')

    class Meta:
        verbose_name = 'Myhmanhana'
        verbose_name_plural = 'Myhmanhanalar'

    def __str__(self):
        return self.name

class Meals(models.Model):
    name = models.CharField(max_length=255,  null=True)
    category = models.CharField(max_length=255,  null=True)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='meals_images',null=True)
    description = models.TextField(null=True)
    created = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Tagam'
        verbose_name_plural = 'Tagamlar'

    def __str__(self):
        return self.name

class Rooms(models.Model):
    name = models.CharField(max_length=255,  null=True,verbose_name='Ady')
    address = models.CharField(max_length=255,  null=True,verbose_name='Salgysy')
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE,verbose_name='Myhmanhana')
    price = models.CharField(max_length=255,  null=True,verbose_name='Bahasy')
    img = models.ImageField(upload_to='room_images',null=True,verbose_name='Suraty')
    description = models.TextField(null=True,verbose_name='Maglumaty')
    created = models.DateField(auto_now_add=True)
    person_place = models.CharField(max_length=50,null=True,verbose_name='Ýer sany')
    bath = models.BooleanField(default=True,verbose_name='Duş')
    car = models.BooleanField(default=True,verbose_name='Awto park')
    bar = models.BooleanField(default=True,verbose_name='Kafe')
    wifi = models.BooleanField(default=True,verbose_name='Wifi')
    sport = models.BooleanField(default=True,verbose_name='Fitness zal')

    class Meta:
        verbose_name = 'Otag'
        verbose_name_plural = 'Otaglar'

    def __str__(self):
        return self.name+" - "+ self.hotel.name

class Hotel_admin(models.Model):
    name = models.CharField(max_length=255,  null=True)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    email = models.CharField(max_length=255,  null=True)
    phone = models.CharField(max_length=255,  null=True)
    male = models.BooleanField(default=True)
    password = models.CharField(max_length=255,  null=True)
    
    class Meta:
        verbose_name = 'Myhmanhana dolandyryjysy'
        verbose_name_plural = 'Myhmanhana dolandyryjylary'

    def __str__(self):
        return self.name

