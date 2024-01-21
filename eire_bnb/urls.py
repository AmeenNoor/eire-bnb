from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('accommodation.urls')),
]

handler404 = 'accommodation.views.error_404_view'

handler500 = 'accommodation.views.handler500'
