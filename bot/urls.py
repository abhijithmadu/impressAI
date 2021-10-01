from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('registration', views.signup, name='registration'),
    path('logout', views.logout, name='logout'),
    path('stupid', views.stupid, name='stupid'),
    path('fat', views.fat, name='fat'),
    path('dumb', views.dumb, name='dumb'),

]
