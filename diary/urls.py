from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('entry/<int:entry_id>/', views.entry_detail, name='entry_detail')
]