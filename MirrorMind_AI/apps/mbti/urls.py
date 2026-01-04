from django.urls import path
from . import views

urlpatterns = [
    path('', views.mbti_view, name='mbti')
]
