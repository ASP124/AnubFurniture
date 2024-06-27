from django.urls import path
from . import views

urlpatterns = [
    path('support/', views.support, name='support'),
    path('subscribe/', views.subscribe_newsletter, name='subscribe_newsletter'),
]
