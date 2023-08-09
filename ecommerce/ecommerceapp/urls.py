from django.urls import path
from ecommerceapp import views


urlpatterns = [
    path('',views.home,name='home'),
    path('login',views.handlelogin,name='handlelogin'),
    path('signup',views.signup,name='signup'),
    path('logout',views.logouts,name='logouts'),
    path('about',views.about,name="about"),
    path('contact/',views.contactus,name='contactus'),
    path('tracker', views.tracker,name="TrackingStatus"),
    path('products/<int:myid>', views.productView, name="ProductView"),
    path('checkout/', views.checkout,name="Checkout"),
    path('handlerequest/', views.handlerequest,name="HandleRequest"),
    path('activate/<uidb64>/<token>',views.ActivateAccountView.as_view(),name='activate'),

]