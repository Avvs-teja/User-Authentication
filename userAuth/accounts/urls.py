from django.contrib import admin
from django.urls import path
from . import views
from .views import logout_view


urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('register/', views.register, name='register'),
    path('', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('app/', views.app, name='app'), 
    path('logout/', logout_view, name='logout'),

]
