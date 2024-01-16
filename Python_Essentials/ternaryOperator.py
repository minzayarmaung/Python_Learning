# In this program , I'm going to share about Ternary Operator.
# Credit goes to Medium Aricle

# A normal if elif Block 

score = 50

if score > 90 :
    print("Great !")
elif score <= 70 :
    print("Average !")
elif score > 20 and score < 40:
    print("Pass !")
else:
    print("Failed !")
    

# "Using the Ternary Operator"

score1 = 55

grade = "Grade - A" if score1 > 90 else "Pass" if score > 50 else "Fail"