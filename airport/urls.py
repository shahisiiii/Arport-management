"""
URL configuration for airport project.

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
from apps.airportapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add/', views.airport_create_view, name='airport_add'),
    path('list/', views.airport_list_view, name='airport_list'),
    path('find-last-child/', views.find_last_child_airport, name='find_last_child_airport'),
    path('find-longest-duration/', views.find_longest_duration, name='find_longest_duration'),
    path('find-shortest-duration/', views.find_shortest_duration, name='find_shortest_duration'),


]





