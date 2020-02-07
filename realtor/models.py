from django.db import models
from datetime import datetime
# Create your models here.
class Realtor(models.Model):
    name=models.CharField(max_length=200)
    contact=models.CharField(max_length=12)
    email=models.EmailField()
    photo=models.ImageField(upload_to='photo')
    hire_date=models.DateTimeField(default=datetime.now,blank=True)
    is_som=models.BooleanField(default=False)
    def __str__(self):
        return self.name
