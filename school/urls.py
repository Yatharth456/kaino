from django.urls import path
from .views import *
from .student_views import *
from .admin_views import *
from .teacher_view import *

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('signup/', RegisterAPI.as_view(), name='signup'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('request/', RequestAccessAPI.as_view(), name='request'),
    path('change_pswd/', PasswordChange.as_view(), name='change_pswd'),
    
    #Student Urls==================
    path('std_profile/', StudentProfileView.as_view(), name='std_profile'),

    #Admin Urls====================
    path('create_school/', CreateSchoolView.as_view(), name='create_school'),
    path('course/', CreateLession.as_view(), name='create_course'),
    path('session/', TermSystem.as_view(), name='create_session'),
    path('role_change/', ChangeRole.as_view(), name='role_change'),

    #Teacher Urls==================
    path('profile/', TeacherProfileView.as_view(), name='profile'),
    path('get_teachers/', GetTeachers.as_view(), name='get_teachers')

]