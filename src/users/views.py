from django.shortcuts import render, get_object_or_404
from .serializers import RegisterSerializer, ProfileSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Profile
import json.decoder


@api_view(['GET','POST'])
def register_view(request):
    if request.method == 'GET':
        serializer = RegisterSerializer()
        
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return  Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT'])
def profile_view(request):
    profile = get_object_or_404(Profile,user = request.user )
    if request.method == 'GET':
         serializer = ProfileSerializer(profile)
         return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProfileSerializer(profile,data= request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                    'message':'This Profile updated succesfully'
                   }
            return Response(data,status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
        

