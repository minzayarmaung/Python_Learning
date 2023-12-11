student_scores = {
    "Harry" : 81,
    "Ron" : 78,
    "Hermione" : 99,
    "Draco" : 74,
    "Neville" : 64
}

student_grades = {}

for grades in student_scores:
    if student_scores[grades] > 90 and student_scores[grades] <= 100:
        student_grades[grades] = "Outstanding" 
    if student_scores[grades] > 80 and student_scores[grades] <= 90:
        student_grades[grades] = "Exceeds Expectations"
    if student_scores[grades] > 70 and student_scores[grades] <=80:
        student_grades[grades] = "Acceptable"
    if student_scores[grades] < 70 :
        student_grades[grades] = "Fail"
        
print(student_grades)