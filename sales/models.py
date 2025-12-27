from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=255,null=True,blank=True)
    availability = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
    