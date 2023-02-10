from django.urls import path, include
from . import views

app_name='sampleapp'
urlpatterns = [
    path('', views.MyCreateView.as_view(), name='create'),
]