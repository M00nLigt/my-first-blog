from django.urls import path
from . import views, views2

urlpatterns = [
    path('', views.index),
    path('pdf',views.getpdf),


]
