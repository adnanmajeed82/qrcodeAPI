from django.shortcuts import render

from rest_framework import generics
from .serializers import *
from .models import *

class ListToDo(generics.ListAPIView):  #Read
    queryset=images.objects.all()
    serializer_class=ImagesSerializer

class DetailTodo(generics.RetrieveUpdateAPIView): #update
    queryset=images.objects.all()
    serializer_class=ImagesSerializer

class CreateTodo(generics.CreateAPIView):  #Create
    queryset=images.objects.all()
    serializer_class=ImagesSerializer

class DeteleTodo(generics.DestroyAPIView):   #Delete
    queryset=images.objects.all()
    serializer_class=ImagesSerializer

  
 

 