from django.db import models
from datetime import datetime
from realtor.models import Realtor
# Create your models here.
class Listing(models.Model):
    realtor=models.ForeignKey(Realtor,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    address=models.CharField(max_length=200)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    zip=models.CharField(max_length=20)
    bedrooms=models.IntegerField()
    bathroom=models.DecimalField(max_digits=2,decimal_places=1)
    price=models.IntegerField()
    garage=models.IntegerField()
    sqrt=models.IntegerField()
    lot_size=models.DecimalField(max_digits=2,decimal_places=1)
    description=models.TextField()
    listing_date=models.DateTimeField(default=datetime.now,blank=True)
    main_photo=models.ImageField(upload_to='photo/')
    main1=models.ImageField(upload_to='photo/',blank=True)
    main2=models.ImageField(upload_to='photo/',blank=True)
    main3=models.ImageField(upload_to='photo/',blank=True)
    main4=models.ImageField(upload_to='photo/',blank=True)
    main5=models.ImageField(upload_to='photo/',blank=True)
    main6=models.ImageField(upload_to='photo/',blank=True)
    is_published=models.BooleanField(default=True)
    def __str__(self):
        return self.title
