from django.urls import path
from sharpauth import views

urlpatterns = [
    path('signup/', views.signup, name='signup')
]
