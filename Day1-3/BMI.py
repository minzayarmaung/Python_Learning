print("Welcome to our BMI Calculator !")

weight = input("Enter your Weight in Kg : ")
height = input("Enter your Height : ")

bmi = int(weight) / float(height)**2
bmi_as_int = int(bmi)

print(bmi_as_int)