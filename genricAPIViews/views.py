from django.shortcuts import render
from api.serializers import StudentModelSeralizer
from api.models import Student

# Generic APIView and Model MIxins
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import (ListModelMixin, 
CreateModelMixin, RetrieveModelMixin, UpdateModelMixin,
DestroyModelMixin)

#all in one methods

#list and create - no pk is required
class LCStudentAPI(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSeralizer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
#update and delete - pk required
class UDStudentAPI(UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin ,GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSeralizer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


#individual methods
class StudentList(ListModelMixin ,GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSeralizer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class StudentCreate(CreateModelMixin ,GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSeralizer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class StudentRetrieve(RetrieveModelMixin ,GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSeralizer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

class StudentUpdate(UpdateModelMixin ,GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSeralizer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

class StudentDelete(DestroyModelMixin ,GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSeralizer

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)