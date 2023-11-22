print("Welcome to the Program")

number = int(input("Enter your height in cm to check : "))
bill = 0

if(number >= 120):
    print("You can ride!")
    age = int(input("What's your age? : "))
    if age < 12 :
        bill = 5
        print("Ticket Price : $5")
    elif age <= 18:
        bill = 7
        print("Ticket Price :  $7")
    elif age >=45 and age <= 55:
        print("Everything's gonna be okay. Have a free ride on Us !")
    else:
        bill = 12
        print("Ticket Price : $12")
        
    wants_photo = input("Do you want Photo Service ?  Y or N.")
    if wants_photo == "Y":
        bill += 3
        
        print(f"Your Final Bill is ${bill}")
else:
    print("You cannot ride")