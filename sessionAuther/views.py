from django.shortcuts import render
from api.serializers import StudentModelSeralizer
from api.models import Student
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly
from rest_framework import viewsets
from .customPermissons import MyCustomPermissions

#fuction based api-views
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status


class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentModelSeralizer
    authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticated]
    # permission_classes = [IsAdminUser]
    # permission_classes = [IsAuthenticatedOrReadOnly]
    # permission_classes = [DjangoModelPermissions]
    # permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    permission_classes = [MyCustomPermissions]

@api_view(['GET','POST','PUT','PATCH','DELETE'])
@authentication_classes([SessionAuthentication])
@permission_classes([MyCustomPermissions])
def student_api_fn(request, pk=None):
    if request.method == 'GET':
        id = pk
        if id is not None:
            stu = Student.objects.get(id = id)
            serializer = StudentModelSeralizer(stu)
            return Response(serializer.data)
        stu = Student.objects.all()
        serializer = StudentModelSeralizer(stu, many=True)
        return Response(serializer.data)