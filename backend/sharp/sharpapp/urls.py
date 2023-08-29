from django.urls import path
from sharpapp import views

urlpatterns = [
    path('',views.index, name='index')
]
