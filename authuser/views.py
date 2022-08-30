from django.shortcuts import render

# Create your views here.

from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response

@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):

    username = request.data.get("username")
    password = request.data.get("password")    
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)                        
    user = authenticate(username=username, password=password)       
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)                        
                        
    token, _ = Token.objects.get_or_create(user=user)      
    return Response({'token': token.key},
                    status=HTTP_200_OK)
 
 
@api_view(["POST"])
def resetpassword(request):
    username = request.data.get("username")
    password = request.data.get("password")
    newpassword = request.data.get("newpassword")    
    if username is None or password is None or newpassword is None:
        return Response({'error': 'Please provide username ,password and new password'},
                        status=HTTP_400_BAD_REQUEST)                        
    user = authenticate(username=username, password=password)    
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)                 
        
    user.set_password(newpassword)
    user.save()    
    return Response({'Password Updated successfully'},
                    status=HTTP_200_OK)  
                    
                    
                    
@api_view(["POST"])
def logout(request):
    
    request.user.auth_token.delete()
    
    #logout(request)
    
    return Response({'User logged out successfully'},
                    status=HTTP_200_OK)                 
                    
