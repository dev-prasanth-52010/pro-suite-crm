from rest_framework import serializers
from django.contrib.auth import get_user_model


User = get_user_model()

class SignupSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    class Meta:
        fields = ["email","password"]
        model = User