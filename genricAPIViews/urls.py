from django.urls import path
from .views import *
urlpatterns = [
    path('studentapi/', StudentList.as_view()),
    # path('studentapi/', StudentCreate.as_view()),
    # path('studentapi/<int:pk>/', StudentRetrieve.as_view()),
    # path('studentapi/<int:pk>/', StudentUpdate.as_view()),
    path('studentapi/<int:pk>/', StudentDelete.as_view()),
    path('lcstudentapi/', LCStudentAPI.as_view()),
    path('udstudentapi/<int:pk>/', UDStudentAPI.as_view()),
]
