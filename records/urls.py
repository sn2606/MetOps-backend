from django.urls import path

from . import views


urlpatterns = [
    path('view/', views.record_detail_view),
    path('create/', views.record_create_view),
]
