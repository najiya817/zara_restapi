"""
URL configuration for logapi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api.views import *
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views



router=DefaultRouter()
router.register('prod',ProductModelView,basename="pro")
router.register('brnd',BrandModelView,basename="bnd")
router.register('cat',categoryModelView,basename="catgory")


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('customer/',CustView.as_view()),
    path('tauth/',views.obtain_auth_token),
    # path('prod/<int:id>',get_brand)
    # path('products/',ProductView.as_view()),
    # path('products/<int:pid>',ProductView.as_view()),
    # path('cat/',categoryView.as_view()),
    path('log/',log),
    path('reg/',Registr),
    path('ver/',verify),
]+router.urls 