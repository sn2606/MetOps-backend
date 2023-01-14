from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.api_home),
    path('records/', include('records.urls')),
    path('query/', include('query.urls')),
    path('users/', include('users.urls')),
]
