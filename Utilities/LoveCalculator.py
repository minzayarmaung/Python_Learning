print("Welcome to the Love Calculator !") 

name1 = input("What is your name?\n")
name2 = input("What is their name? \n")

combined_String = name1 + name2
lowercase_String = combined_String.lower()

t = lowercase_String.count("t")
r = lowercase_String.count("r")
u = lowercase_String.count("u")
e = lowercase_String.count("e")

true = t + r + u + e

l = lowercase_String.count("l")
o = lowercase_String.count("o")
v = lowercase_String.count("v")
e = lowercase_String.count("e")

love = l + o + v + e

love_score = int(str(true) + str (love))


if(love_score < 10) or (love_score > 90):
    print(f"Your love score is {love_score}, you guys go together like Cola and Mentos")
elif(love_score >= 40) and (love_score <=50):
    print(f"Your Score is {love_score}, you guys are alright together!")
else:
    print(f"Your Score is {love_score}")


