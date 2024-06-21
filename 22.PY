


def assign_grade(score):
    if score >= 80 and score <= 100:
        return 'A'
    elif score >= 70 and score < 80:
        return 'B'
    elif score >= 60 and score < 70:
        return 'C'
    elif score >= 50 and score < 60:
        return 'D'
    elif score >= 0 and score < 50:
        return 'F'
    else:
        return 'Invalid score' 


scores = [85, 73, 64, 55, 42, 105]
for score in scores:
    print(f"Score: {score}, Grade: {assign_grade(score)}")
