from django.shortcuts import render

# Create your views here.
def mbti_view(request):
    return render(request, 'mbti_test.html')