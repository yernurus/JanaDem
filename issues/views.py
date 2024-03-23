from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import Issue

# Create your views here.
class IssueModelViewSet(viewsets.ModelViewSet):
    queryset = Issue.objects.all()
    
    http_method_names = ['get', 'post', 'patch', 'delete']