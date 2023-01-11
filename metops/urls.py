from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api/records/', include('records.urls')),
    path('api/query/', include('query.urls')),
]
