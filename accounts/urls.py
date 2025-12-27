
from django.urls import path

from .views import SignupAPIView,LoginAPIView,UserDetailsAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("signup/",SignupAPIView.as_view(),name="signup"),
    path("login/",LoginAPIView.as_view(),name="signup"),
    path("users/",UserDetailsAPIView.as_view(),name="signup"),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),    

]