print("Welcome to Leap Year Calculator")

number = int(input("What is the Year? : "))

if number % 4 == 0:
    if number % 100 == 0:
        if number % 400 == 0:
            print("It is a Leap Year")
        else:
            print("It is not a Leap Year")
    else:
        print("It is a Leap Year")
else:
    print("It is not a Leap Year")
