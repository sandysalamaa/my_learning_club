from django.shortcuts import render
from .models import *
from rest_framework.viewsets import ModelViewSet

# Create your views here.
class ChatViewSet(ModelViewSet):
    queryset = ChatGroup.objects.all()
    
