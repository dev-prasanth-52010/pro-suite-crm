from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework import status
from rest_framework.response import Response
from .models import Contacts
from .serializers import ContactSerializer
from rest_framework.authentication import BaseAuthentication
from rest_framework.permissions import AllowAny

class ContactAPIView(CreateAPIView):
    serializer_class = ContactSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        return Response({
            "results":{},
            "message":"contact saved.",
            "sucess":"true",
        })