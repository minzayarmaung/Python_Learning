print("Welcome to BMI Calculator!")

weight = float(input("What's your Weight in KG? : "))
height = float(input("What's your Height? : "))

bmi = weight / height**2
bmi_as_int = int(bmi)

print(bmi_as_int)

if bmi_as_int <= 1.85:
    print("Underweight")
elif 1.85< bmi_as_int <25:
    print("Normal Weight")
elif 25< bmi_as_int <30:
    print("Over Weight")
elif 30<= bmi_as_int <35:
    print("Obese")
elif bmi_as_int >= 35:
    print("You Fat ass Nigga")