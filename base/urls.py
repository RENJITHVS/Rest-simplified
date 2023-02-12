
from django.contrib import admin
from django.urls import path, include
from api import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('celerytask.urls')),
    path('api-gen/', include('genricAPIViews.urls')),
    path('api-con/', include('concreteAPIView.urls')),
    path('api-modvs/', include('modelViewSet.urls')),
    path('api-viewset/', include('viewsetClass.urls')),
    path('api-bap/', include('basicAuthPermiss.urls')),
    path('api-sauth/', include('sessionAuther.urls')),
    path('api-tauth/', include('TokenAuther.urls')),
    path('api-jwtauth/', include('jwtAuthApp.urls')),
    # jwt default setup
    path('gettoken/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refreshtoken/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verifytoken/', TokenVerifyView.as_view(), name='token_verify'),
    ###
    path('studentinfo/<int:pk>/', views.student_detail),
    path('studentlist/', views.student_list),
    path('studentcreate/', views.student_create),
    path('studentapi/', views.student_api,name="student-view"),
    path('student-cls-api/', views.StudentAPI.as_view(),name="studnet_cls_api"),
    path('hello-w/', views.hello_word , name="hellow"),
    path('student-api-fn/', views.student_api_fn , name="student_api_fn"),
    path('student-api-fn/<int:id>/', views.student_api_fn , name="student_api_fn"),
    path('student-api-cls/', views.StudentClassAPI.as_view() , name="student_api_clss_full"),
    path('student-api-cls/<int:id>/', views.StudentClassAPI.as_view() , name="student_api_clss"),
    
]
