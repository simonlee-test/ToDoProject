from django.urls import path, include
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name="Homepage"),
    path('api/', include('api.urls')),
]
