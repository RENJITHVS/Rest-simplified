from django.urls import path
from .views import *

urlpatterns = [
    path('studentapi/', StudentListCreate.as_view()),
    path('studentapi/<int:pk>/', StudentRetrieveUpdateDestroy.as_view()),
]