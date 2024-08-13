student_scores = {
    "John" : 90,
    "Edy" : 68,
    "Marry" : 88,
    "Ewan" : 79,
    "Park" : 62,
}

# TODO    
def convert_grade(student_scores):
    conversion = {}
    for name in student_scores:
        if student_scores[name] >= 85:
            criteria = "Outstanding"
            conversion[name] = criteria
        elif student_scores[name] >= 65 and student_scores[name] < 85:
            criteria = "Good"
            conversion[name] = criteria
        elif student_scores[name] >= 50 and student_scores[name] < 65:
            criteria = "Acceptable"
            conversion[name] = criteria
        else:
            criteria = "Fail"
            conversion[name] = criteria
    return conversion
    
print(convert_grade(student_scores))