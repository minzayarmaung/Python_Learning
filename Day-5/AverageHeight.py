print("Welcome to Average Height Program")

student_heights = input("Input a List of Student Heights : ").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

print(student_heights)


total_height =  0
for total in student_heights:
    total_height += total


number_of_students = 0
for student in student_heights:
    number_of_students+=1
 
average_height = round(total_height/number_of_students)
print(average_height)