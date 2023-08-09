from django.urls import path
from ecommapp import views


# Defining paths for the urls and redirections


urlpatterns = [
    path('',views.home,name='home'),
    path('Login', views.login,name="login"),
    path('SugnUp', views.signup,name="signup"),
    path('about', views.about,name='about'),
    path('contact/', views.contuctus,name='contactus'),
    path('products/<int:myid>', views.productView, name="ProductView"),
    path('checkout/', views.checkout,name="checkout"),
    path('requests', views.requests,name='requests'),
    path('activate/<uidb64>/<token>',views.ActivateAccountView.as_view(),name='activate'),
]