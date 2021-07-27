
from django.contrib import admin
from django.urls import path, include
from app1 import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app1/', include('app1.urls')),
    path('common/', include('common.urls')),
    path('service/', include('service.urls')),

    path('', views.index, name='index'),
]
