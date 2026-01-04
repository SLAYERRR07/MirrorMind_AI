from django.shortcuts import render

def mbti_view(request):
    return render(request, 'mbti_test.html')