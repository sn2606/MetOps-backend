from django.urls import path

from . import views


urlpatterns = [
    path('', views.get_meteomatics_response),
    path('list/', views.query_list_view),
]
