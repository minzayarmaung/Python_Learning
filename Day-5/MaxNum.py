print("Welcome to Max Number Program")

student_scores = input("Input a list of Students Score : ").split()
for n in range (0, len(student_scores)):
    student_scores[n] =  int(student_scores[n])
    
print(student_scores)

highest_score = 0

for score in student_scores:
    if score > highest_score:
        highest_score = score

print(f"Highest Score : {highest_score}")   