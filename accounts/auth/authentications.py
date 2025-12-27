from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken


def login_user(email,password):
    user = authenticate(username=email,password=password)
    print("User from login user",user)
    if not user:
        return None,None
    
    refresh = RefreshToken.for_user(user=user)
    return user , str(refresh.access_token)