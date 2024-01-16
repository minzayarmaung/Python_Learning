# Tuple Unpacking  ( with & without )

person = ["Tom" , 5 , "USA"]

name , age , country = person

print(f"{name} , {age} , {country}")

# We can use tuple unpacking to assign multiple variables in one line

letters = ["A" , "B" , "C" , "D" , "E" , "F" , "G" , "H"]

firstLetter , secondLetter , *restofLetters = letters

print(f" First : {firstLetter} ,Second : {secondLetter} ,Others : {restofLetters}") 

# We can add (*) character in front of the variables to identify that it contains everything else that hasn't 
# been assigned to other variables.