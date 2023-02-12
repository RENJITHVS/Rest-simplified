from django.shortcuts import render
from api.serializers import StudentModelSeralizer
from api.models import Student

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import viewsets
# Create your views here.
"""
To generate token use
1 - Use django admin panel
2 - from command terminal - 
    python manage.py drf_create_token <username>
3 - By exposing an api endpoint at urls.py
4 - using signals
""" 
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentModelSeralizer
    authentication_classes = [TokenAuthentication]
    # permission_classes = [AllowAny]
    permission_classes = [IsAuthenticated]

