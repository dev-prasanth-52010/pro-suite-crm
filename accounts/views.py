from django.shortcuts import render


from rest_framework.generics import ListCreateAPIView,ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from rest_framework_simplejwt.tokens import RefreshToken,AccessToken
from django.contrib.auth import login,logout,get_user_model,authenticate
from rest_framework.authentication import BaseAuthentication
from rest_framework.permissions import *
from core.auth import CookieJWTAuthentication
from .auth.authentications import login_user
from rest_framework import status

User = get_user_model()
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
    



class LoginAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        user , access_token = login_user(email,password)

        print("******** user : ",user)
        
        if not user:
            response = Response({
                "results": "Login failed",
                "status": "failure",
            },status=status.HTTP_401_UNAUTHORIZED)

        response = Response(
            {"success": True, "message": "Login successful"},
            status=status.HTTP_200_OK
        )
        response.set_cookie(
            key="access",
            value=access_token,
            httponly=True,
            secure=False, 
            samesite="Lax",  
            domain=None, 
            path="/",
            max_age=3600,
        )

        return response

class UserDetailsAPIView(ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [CookieJWTAuthentication]  
    queryset = User.objects.all()

    def get_queryset(self):
        return super().get_queryset()
