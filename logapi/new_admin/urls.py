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
    path('ebnd/<int:pk>',EditBrand.as_view(),name='ebnd'),
    path('pro/',ProductView.as_view(),name='pro'),
    path('addpro/',AddProducts.as_view(),name='addpro'),
    path('editpro/<int:pk>',EditProducts.as_view(),name='editpro'),
    path('ban',BannerView.as_view(),name='ban'),
    path('eban/<int:pk>',EditBanner.as_view(),name='eban'),
]