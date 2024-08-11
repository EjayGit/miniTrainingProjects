student_scores = [80, 60, 50, 65, 75, 55]

def sum_score_above_average(p_student_scores):
    # TODO
    total = 0
    number = 0
    for score in student_scores:
        total += score
        number += 1
    avg = total / number
    total = 0
    number = 0
    for score in student_scores:
        if score > avg:
            total += score
            number += 1
    return total
        
print(sum_score_above_average(student_scores))