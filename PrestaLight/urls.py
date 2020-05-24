
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from LightSpeed import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', views.lightpeed, name='lightspeedPage'),
]
