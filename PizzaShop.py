print("Welcome to Pizza Shop !")
print("What size Pizza do you want ? Small Pizza : $15\n Medium Pizza : $20\n Large Pizza : $25 ")

size = input("What size do you want? What Size do you want ? S , M , L : ")

print("Pepper for Small Pizza : +$2")
print("Pepper for Medium or Large Pizza : +$3")

print("Extra Cheese for any Size Pizza : +$1")

add_pepperoni = input("Do you want extra Pepperoni? Y or N\n")
extra_chesse = input("Do you want Extra Cheese ? Y or N\n")

bill = 0

if size == "S":
    bill = 15
if size =="M":
    bill = 20
if size =="L":
    bill = 25

if add_pepperoni == "Y":
    if size == "S":
        bill+=2
    elif size == "M":
        bill+=3
    elif size =="L":
        bill+=3
if extra_chesse == "Y":
    bill+=1
    
print(f"The final Bill is : {bill}")



