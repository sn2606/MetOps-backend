from django.urls import path

from . import views


urlpatterns = [
    path('view/', views.record_detail_view),
    path('delete/', views.record_delete_view),
]
