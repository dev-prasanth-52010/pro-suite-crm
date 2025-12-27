
from django.urls import path

from .views import ContactAPIView
urlpatterns = [
    path("contacts/",ContactAPIView.as_view(),name="contacts"),


]