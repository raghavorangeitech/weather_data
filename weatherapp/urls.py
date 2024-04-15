from django.urls import path
from .import views

urlpatterns = [
    path('',views.home),
    path('team/', views.team_view, name='team'),
    path('download_csv/', views.download_csv, name='download_csv'),
    
]