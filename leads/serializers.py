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
        

    def validate(self,attrs):
        first_name = attrs.get("first_name")
        last_name = attrs.get("last_name")  

        if not str(first_name).isalpha() and str(last_name).isalpha() :
            raise ValidationError("first , last name contains numeric")
        

        return attrs
    

    def create(self, validated_data):
        return Contacts.objects.create(**validated_data)