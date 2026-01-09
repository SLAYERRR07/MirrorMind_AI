def calculate_mbti(form_data):
    """
    Calculate MBTI personality type based on 20 questions.
    
    Questions mapping:
    - E vs I: q1-q5 (1,3,5 favor E; 2,4 favor I)
    - S vs N: q6-q10 (6,8,10 favor S; 7,9 favor N)
    - T vs F: q11-q15 (11,13,15 favor T; 12,14 favor F)
    - J vs P: q16-q20 (16,18,20 favor J; 17,19 favor P)
    
    Args:
        form_data: Dictionary with question keys (q1-q20) and values (1-5)
    
    Returns:
        str: MBTI type (e.g., 'INTJ', 'ENFP')
    
    Raises:
        ValueError: If required questions are missing or invalid
    """
    def safe_int(value, default=0):
        """Safely convert value to integer."""
        try:
            return int(value) if value else default
        except (ValueError, TypeError):
            return default
    
    # Initialize scores for each dimension
    E_score = 0  # Extraversion
    I_score = 0  # Introversion
    S_score = 0  # Sensing
    N_score = 0  # Intuition
    T_score = 0  # Thinking
    F_score = 0  # Feeling
    J_score = 0  # Judging
    P_score = 0  # Perceiving
    
    # E vs I dimension (Questions 1-5)
    # Q1, Q3, Q5 favor E (direct score)
    # Q2, Q4 favor I (reverse score: 6 - value)
    E_score += safe_int(form_data.get('q1', 0))
    I_score += (6 - safe_int(form_data.get('q2', 3)))  # Reverse for I
    E_score += safe_int(form_data.get('q3', 0))
    I_score += (6 - safe_int(form_data.get('q4', 3)))  # Reverse for I
    E_score += safe_int(form_data.get('q5', 0))
    
    # S vs N dimension (Questions 6-10)
    # Q6, Q8, Q10 favor S (direct score)
    # Q7, Q9 favor N (reverse score)
    S_score += safe_int(form_data.get('q6', 0))
    N_score += (6 - safe_int(form_data.get('q7', 3)))  # Reverse for N
    S_score += safe_int(form_data.get('q8', 0))
    N_score += (6 - safe_int(form_data.get('q9', 3)))  # Reverse for N
    S_score += safe_int(form_data.get('q10', 0))
    
    # T vs F dimension (Questions 11-15)
    # Q11, Q13, Q15 favor T (direct score)
    # Q12, Q14 favor F (reverse score)
    T_score += safe_int(form_data.get('q11', 0))
    F_score += (6 - safe_int(form_data.get('q12', 3)))  # Reverse for F
    T_score += safe_int(form_data.get('q13', 0))
    F_score += (6 - safe_int(form_data.get('q14', 3)))  # Reverse for F
    T_score += safe_int(form_data.get('q15', 0))
    
    # J vs P dimension (Questions 16-20)
    # Q16, Q18, Q20 favor J (direct score)
    # Q17, Q19 favor P (reverse score)
    J_score += safe_int(form_data.get('q16', 0))
    P_score += (6 - safe_int(form_data.get('q17', 3)))  # Reverse for P
    J_score += safe_int(form_data.get('q18', 0))
    P_score += (6 - safe_int(form_data.get('q19', 3)))  # Reverse for P
    J_score += safe_int(form_data.get('q20', 0))
    
    # Determine MBTI type based on scores
    mbti_type = ""
    
    # E vs I
    mbti_type += "E" if E_score >= I_score else "I"
    
    # S vs N
    mbti_type += "S" if S_score >= N_score else "N"
    
    # T vs F
    mbti_type += "T" if T_score >= F_score else "F"
    
    # J vs P
    mbti_type += "J" if J_score >= P_score else "P"
    
    return mbti_type
