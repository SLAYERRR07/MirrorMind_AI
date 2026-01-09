from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .services import calculate_mbti

@login_required
def mbti_test_view(request):
    """
    Renders the MBTI test page and processes the form submission.
    Calculates personality type and saves it to the user's profile.
    """
    if request.method == 'POST':
        # Extract form data
        form_data = request.POST.dict()
        form_data.pop('csrfmiddlewaretoken', None)
        
        # Validate that all 20 questions are answered
        answered_questions = [key for key in form_data.keys() if key.startswith('q')]
        if len(answered_questions) < 20:
            messages.error(request, 'Please answer all 20 questions before submitting.')
            return render(request, 'mbti_test.html')
        
        # Calculate personality using the service function
        try:
            mbti_type = calculate_mbti(form_data)
            
            # Update the logged-in user's personality fields
            user = request.user
            user.mbti_type = mbti_type
            user.personality_type = mbti_type  # Store in both fields
            user.save()
            
            messages.success(request, f'Your MBTI type is: {mbti_type}')
            return redirect('dashboard')  # Redirect to dashboard after successful submission
        except Exception as e:
            messages.error(request, f'An error occurred while calculating your personality type: {str(e)}')
            return render(request, 'mbti_test.html')
    
    # GET request - render the test page
    return render(request, 'mbti_test.html')
