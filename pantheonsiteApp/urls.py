from django.urls import path
from . import views

app_name = 'pantheonsiteApp'

urlpatterns = [
    path('', views.home, name='companies'),
    path('detail/', views.detail, name='detail'),
]


