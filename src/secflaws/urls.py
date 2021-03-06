from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:secret_id>/', views.details, name='details'),
    path('add/', views.addSecret, name='add'),
]