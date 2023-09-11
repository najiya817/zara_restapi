from django.urls import path
from  .views import *

urlpatterns = [
    path('',home),
    path('logi/',login_view,name='logi'),
    path('regi/',reg_view,name='reg'),
    path('edit/<int:pk>',EditCategory.as_view(),name='edit'),
    path('lhome/',LandHome,name='h'),
    path('catgry/',CategoryView.as_view(),name='catg'),
    path('bnd/',BrandView.as_view(),name='bnd'),
    path('ebnd/<int:pk>',EditBrand.as_view(),name='ebnd')
]