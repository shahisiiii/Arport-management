from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.airport_create_view, name='airport_add'),
    path('list/', views.airport_list_view, name='airport_list'),

]
