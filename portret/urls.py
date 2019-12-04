from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='portret-home'),
    path('home/', views.home, name='portret-home'),
    path('overmij/', views.overmij, name='portret-overmij'),
    path('cv/', views.cv, name='portret-cv')
]