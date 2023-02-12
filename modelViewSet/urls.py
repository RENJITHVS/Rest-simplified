from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

# Creating ROuter object
router = DefaultRouter()

#regoister student viewset with Router 
#no need of paramters
router.register('studentapi', StudentModelViewSet, basename='student')
router.register('studentapiro', ReadOnlyStudentModelViewSet, basename='studentro')

urlpatterns = [
    path('', include(router.urls))
]