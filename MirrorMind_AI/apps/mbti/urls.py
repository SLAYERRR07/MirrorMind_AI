from django.urls import path
from . import views

urlpatterns = [
    path('', views.mbti_test_view, name='mbti_test')
]
