from django.urls import path
from  .views import *

urlpatterns = [
    path('',home),
    path('logi/',login_view,name='logi'),
    path('regi/',reg_view,name='reg'),
    path('lhome/',LandHome,name='h')
]