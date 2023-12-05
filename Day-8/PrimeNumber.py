print("Welcome to Prime Numbers Program")

def prime_checker(number):
    is_Prime = True
    for i in range(2 , number):
        if number % i == 0:
            is_Prime = False
            
    if is_Prime:
             print(f"{number} is a Prime Number.")
    else:
            print(f"{number} is not a Prime Number.")

number = int(input("Enter a Number : "))
prime_checker(number)       
        