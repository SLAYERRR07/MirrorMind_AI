from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
    path('chat/', views.ai_chatbot_view, name='ai_chatbot')
]
