"""office URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
#from career.views import career , career_applicant, ApplicationView, view_career
from career.views import add_show, update_data, delete_data, view_applicant,index,ApplicationView2
# from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('delete/<int:id>/',delete_data, name="deletedata"),
    path('<int:id>/',update_data, name="updatedata"),
    #path("view_career/", view_career, name="view_career"),
    #path("career/", career, name="career"),
    # path("career_applicant/", career_applicant, name="career_applicant"),
    path("view_applicant/", view_applicant, name="view_applicant"),
    # path("ApplicationView/<int:myid>", ApplicationView, name="ApplicationtView"),
    path("ApplicationView2/<int:myid>", ApplicationView2, name="ApplicationtView2"),
    path("career_show/", add_show, name="add"),
    path("index/", index, name="index"),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)