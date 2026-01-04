from django.shortcuts import render

def dashboard_view(request):
    return render(request, 'dashboard.html')

def ai_chatbot_view(request):
    return render(request, 'ai_chatbot.html')