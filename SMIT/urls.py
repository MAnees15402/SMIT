"""
URL configuration for SMIT project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from SMIT import views

admin.site.site_header = 'Developer Anees'
admin.site.site_title = ' Welcom to M.Anees Dashboard'
admin.site.index_title = 'Welcom to Portal'


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('course/', views.course, name='course'),
    path('projact/', views.projact, name='projact'),
    path('contact/', views.contact, name='contact'),
 # Corrected the function name

]

