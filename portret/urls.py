from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='portret-home'),
    path('home/', views.home, name='portret-home'),
    path('info/', views.info, name='portret-info'),
    path('cv/', views.cv, name='portret-cv'),
    path('contact/', views.contact, name ='portret-contact')
]