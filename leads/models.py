from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
import uuid
User = get_user_model()



class Auditlog(models.Model):
    is_active = models.BooleanField(default=True,null=True,blank=True)
    is_archive = models.BooleanField(default=False,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True,null=True,blank=True)
    history = models.JSONField(default=dict,null=True,blank=True)
    slug = models.SlugField(null=True,blank=True)

    def __str__(self):
        return self.id
    
    class Meta:
        abstract = True

class Program(models.Model):
    name = models.CharField(max_length=255,null=True,blank=True)


class Elective(models.Model):
    name = models.CharField(max_length=255,null=True,blank=True)



class Contacts(Auditlog):
    first_name = models.CharField(max_length=255,null=True,blank=True)
    last_name = models.CharField(max_length=255,null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    phone = models.CharField(max_length=20,blank=True,null=True)
    age = models.IntegerField(null=True,blank=True)
    dob = models.DateField(null=True,blank=True)
    course = models.CharField(max_length=20,blank=True,null=True)
    program = models.ForeignKey(Program,on_delete=models.SET_NULL,blank=True,null=True,related_name="contacts")
    elective = models.ForeignKey(Elective,on_delete=models.SET_NULL,blank=True,null=True,related_name="contacts")
    utm_source  = models.CharField(max_length=255,blank=True,null=True)
    utm_medium  = models.CharField(max_length=255,blank=True,null=True)
    utm_campaign  = models.CharField(max_length=255,blank=True,null=True)
    utm_device  = models.CharField(max_length=255,blank=True,null=True)
    

    def __str__(self):
        return str(self.id)
    
    def save(self,*args,**kwarg):
        if self.slug:
            self.slug = f"CNT-{slugify(uuid.uuid4())}"
        return super().save(*args,**kwarg)