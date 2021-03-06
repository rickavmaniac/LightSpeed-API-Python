
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from LightSpeed import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', views.lightpeed, name='lightspeedPage'),
    path('', views.home, name='homePage'),
    path('item/', views.item, name='ls_item'),
    path('ordertoprocess/', views.order_to_process, name='ordertoprocess'),
]
