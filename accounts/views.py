from django.shortcuts import render


from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import SignupSerializer


class SignupAPIView(APIView):
    def post(self,request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "results":"account created.",
                "status":"success",
                "data":serializer.data
            })
        return Response({
                "results":"account not created.",
                "status":"success",
                "data":serializer.errors
            })