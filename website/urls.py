from django.contrib import admin
from django.urls import path, include
from buddy import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('buddy/', include('buddy.urls')),
    path('', views.buddymainredirect, name='buddymainredirect'),
]
