from django.urls import path,re_path
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
    path('sroute/sregister/',views.sregister,name="sregister"),
    path('troute/tlogin/upload_success/',views.upload_success,name="upload_success"),
    path('troute/tlogin/add_course/',views.add_course,name="add_course"),
    path('troute/tlogin/view_course/',views.view_course,name="view_course"),
    path('troute/tlogin/logout/',views.tlogout,name="tlogout"),
    path('sroute/slogin/view_course/',views.view_course,name="view_course"),
    path('sroute/slogin/logout/',views.slogout,name="slogout"),
    re_path(r'^sroute/slogin/view_course/[a-zA-Z0-9]+',views.count,name="count"),
    path('add_count/',views.add_count,name="add_count"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 
