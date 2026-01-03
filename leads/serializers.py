from rest_framework import serializers
from .models import Contacts
from rest_framework.validators import ValidationError


class ContactSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=True,allow_null=False)
    class Meta:
        model = Contacts
        fields = ["first_name","last_name",
                  "email","phone","dob",
                  "utm_source","utm_medium","utm_campaign",
                  "history","course","elective","program"]  
        

   
    def validate_first_name(self, value):
        if not value.isalpha():
            raise ValidationError("First name cannot contain numbers or special characters.")
        return value

    def validate_last_name(self,value):
        if not value.isalpha():
            raise ValidationError("name can't contains numeric")
        return value
