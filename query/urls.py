from django.urls import path

from . import views


urlpatterns = [
    path('', views.query_response_view),
    path('list/', views.query_list_view),
    path('save/', views.query_save_view),
]
