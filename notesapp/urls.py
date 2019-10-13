from django.urls import path
from django.contrib import admin
from django.conf.urls.static import static
from daproject import settings
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('troute/',views.troute,name="troute"),
    path('sroute/',views.sroute,name="sroute"),
    path('troute/tlogin/upload/',views.upload,name="upload"),
    path('troute/tlogin/',views.tlogin,name="tlogin"),
    path('sroute/slogin/',views.slogin,name="slogin"),
    path('troute/tregister/',views.tregister,name="tregister"),
    path('troute/sregister/',views.sregister,name="sregister"),
    path('troute/tlogin/upload_success/',views.upload_success,name="upload_success"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

