from django.shortcuts import render
from api.serializers import StudentModelSeralizer
from api.models import Student

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import viewsets

from rest_framework_simplejwt.authentication import JWTAuthentication
# Create your views here.

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentModelSeralizer
    authentication_classes = [JWTAuthentication]
    # permission_classes = [AllowAny]
    permission_classes = [IsAuthenticated]

