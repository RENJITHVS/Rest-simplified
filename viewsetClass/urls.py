from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

# Creating ROuter object
router = DefaultRouter()

#regoister student viewset with Router 
#no need of paramters
router.register('studentapi', StudentViewSet, basename='student')

urlpatterns = [
    path('', include(router.urls))
]
