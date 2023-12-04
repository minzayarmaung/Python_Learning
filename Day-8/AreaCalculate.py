import math

print("Welcome to Area Calculating Program !")

def paint_calc(height , width , cover):
    number_of_cans = (height * width) / cover
    result = math.ceil(number_of_cans)
    print(f"You'll need {result} cans of paint.")

height = int(input("Height of the wall : "))
width = int(input("Width of the wall : "))
coverage = 5

paint_calc(height , width , coverage)

    