from django.shortcuts import render
from api.serializers import StudentModelSeralizer
from api.models import Student
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import viewsets

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentModelSeralizer
    authentication_classes = [BasicAuthentication]
    permission_classes = [AllowAny]