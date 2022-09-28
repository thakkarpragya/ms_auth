from django.shortcuts import render
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

# Create your views here.

@csrf_exempt                    
@api_view(["GET"])
@permission_classes((AllowAny,))
def validate(request):

    token = request.headers.get('Authorization').split("Token ")[1] if request.headers.get('Authorization') is not None else ''

    if token and Token.objects.filter(pk=token).exists():
        return Response(
                {"authorized"},
                status=HTTP_200_OK
                )

    return Response({'User token not found'},
                    status=HTTP_404_NOT_FOUND)
