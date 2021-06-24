from django.urls import path
from . import views

urlpatterns = [
    path('',views.login,name='index.html'),
    path('register',views.register,name='signup.html')
]