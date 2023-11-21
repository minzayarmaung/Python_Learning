print("Welcome to the Tip Calculator")

bill = float(input("What was the total Bill? : "))

tip = int(input("What percentage tip would you like to give? 10 , 12 or 15? : "))

people = int(input("How many people to split the bill? : "))

tip_Amount = bill * (tip/100)
totalAmount = bill + tip_Amount

Each_to_Pay = round(totalAmount / people , 2)

print(f"Each person should pay : ${Each_to_Pay}")

