"""wyreflowtask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from os import name
# from django.contrib import admin
from django.urls import path
from Head import views

urlpatterns = [
    
    path('login/',views.Login,name='login'),
    path('checklogin',views.CheckAdminLogin),
    path('logout/',views.Logout,name='logout'),

    path('dashboard/',views.Dashboard,name='dashboard'),

    path('myteam/',views.Myteam,name='myteam'),
    path('ouremployee/',views.Ouremployee,name='ouremployee'),
    path('head-addnewemployee',views.Addnewemployee,name='head-addnewemployee'),
    path('changepassword',views.Update_Password,name='changepassword'),
    
    path('updateprofile',views.Updateprofile,name='updateprofile'),
    path('updateprofilepicture',views.UpdateProfilePicture,name='updateprofilepicture'),
     path('productview/',views.ProductView,name='product-view'),
    path('modalcustomerview/',views.ModalCustomerView,name='customer-view'),
    path('modalsoldproductview/',views.ModalSoldProductView,name='sold-product-view'),
 path('complainlist/',views.complainlist,name='complainlist'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('other_complains/',views.other_complains,name='other_complains'),
    






]