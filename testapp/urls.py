from django.urls import path, include
from .views import *
urlpatterns = [
    path('seed/', seed),
    path('', test),
]
