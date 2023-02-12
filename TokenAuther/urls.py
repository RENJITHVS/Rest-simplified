from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import  obtain_auth_token
from .auth import CustomAuthToken
# Creating ROuter object
router = DefaultRouter()

#regoister student viewset with Router 
#no need of paramters
router.register('studentapi', StudentModelViewSet, basename='student')


urlpatterns = [
    path('', include(router.urls)),
    # path('gettoken/',obtain_auth_token),
    path('gettoken/', CustomAuthToken.as_view()),
]