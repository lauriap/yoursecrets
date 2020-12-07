from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:secret_id>/', views.secret, name='secret'),
    path('<int:secret_id>/results/', views.results, name='results'),
]