from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def dashboard_view(request):
    user = request.user
    context = {
        'user': user,
        'mbti_type': user.mbti_type or user.personality_type or 'Not Set',
    }
    return render(request, 'dashboard.html', context)

def ai_chatbot_view(request):
    return render(request, 'ai_chatbot.html')