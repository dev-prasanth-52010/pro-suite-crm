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
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "results":{},
                "message":"contact saved.",
                "sucess":"true",
            },status=status.HTTP_201_CREATED)
        return Response({
            "results":{},
            "message":serializer.errors,
            "code":400
        },status=status.HTTP_400_BAD_REQUEST)