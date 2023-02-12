from django.shortcuts import render
from api.serializers import StudentModelSeralizer
from api.models import Student

#view set imports
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

class StudentViewSet(viewsets.ViewSet):
    def list(self, request):
        stu = Student.objects.all()
        serializer = StudentModelSeralizer(stu, many= True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        if pk is not None:
            stu = Student.objects.get(id = pk)
            serializer = StudentModelSeralizer(stu)
            return Response(serializer.data)

    def create(self, request):
        serializer = StudentModelSeralizer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': "partial data updated"})
        return Response(serializer.errors)

    def destroy(self, request, pk=None):
        stu = Student.objects.get(id = pk)
        stu.delete()
        return Response({'msg': 'Data deleted'})


