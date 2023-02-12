from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

# Creating ROuter object
router = DefaultRouter()

#regoister student viewset with Router 
#no need of paramters
router.register('studentapi', StudentModelViewSet, basename='student')
# router.register('studentapifn', student_api_fn, basename='student_fn')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('studentapifn/',student_api_fn, name='student-fn'),
    path('studentapifn/<int:pk>/',student_api_fn, name='student-fn')
]