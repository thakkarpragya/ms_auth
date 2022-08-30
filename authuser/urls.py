#from django import views
from django.urls import path
from .views import *

urlpatterns = [   
    path('api/login', login),
    path('api/logout', logout),
    path('api/resetpassword', resetpassword)
]
