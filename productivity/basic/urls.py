from django.urls import include, path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.login_user),
    path('app', views.app),

    path('admin/', admin.site.urls)

]