from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
# Creating ROuter object
router = DefaultRouter()

#regoister student viewset with Router 
#no need of paramters
router.register('studentapi', StudentModelViewSet, basename='student')


urlpatterns = [
    path('', include(router.urls)),
]

"""
to get request using token:
http http://127.0.0.1:8000/api-jwtauth/studentapi/'Authorization:Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc2MjE3NTQxLCJpYXQiOjE2NzYyMTcyNDEsImp0aSI6ImUwY2RmNTJmMDNkYTRjMTM5ZmFlOTI3NmE2MjZiYjQ5IiwidXNlcl9pZCI6M30.LlRrj0RF0MScopbnTXXTNtO9jsahXPFzXTknwX-1GHc
"""