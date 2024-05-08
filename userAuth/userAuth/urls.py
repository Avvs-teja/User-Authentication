# userAuth/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('accounts.urls')),  # Redirect root URL to accounts app
    path('admin/', admin.site.urls),
]
