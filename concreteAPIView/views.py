from django.shortcuts import render
from api.serializers import StudentModelSeralizer
from api.models import Student


# Concreate API views
from rest_framework.generics import (ListAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView,RetrieveAPIView, ListCreateAPIView,
RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView, RetrieveDestroyAPIView )

class StudentListCreate(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSeralizer

# class StudentList(ListAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentModelSeralizer

class StudentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSeralizer

