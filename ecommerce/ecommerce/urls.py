from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from django.shortcuts import redirect
    


admin.site.site_header = "SharpJr_Trends"
admin.site.site_title = "SharpJr_trends"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('ecommerceapp.urls')),

    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)