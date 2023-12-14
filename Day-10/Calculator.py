import logo
#Calculator

print(logo.logo)

#Adding two Numbers
def adding(n1 , n2):
    return n1+n2

#Substracting two Numbers
def substraction(n1,n2):
    return n1-n2

#Multiplication two Numbers
def multiply(n1,n2):
    return n1*n2

#Dividing two Numbers
def division(n1,n2):
    return n1/n2

operations = {
    "+": adding ,
    "-":substraction,
    "*":multiply,
    "/":division
}

def calculator():
    num1 =float(input("Enter the First Number : "))
    for operator in operations:
        print(operator)       
        
    continue_Calculation = True

    while continue_Calculation:
        operation_symbol = input("Pick an Operator : ")
        num2 = int(input("What's the next Number : "))
        calculation_function = operations[operation_symbol] 
        answer = calculation_function(num1 , num2)
        
        print(f"{num1} {operation_symbol} {num2} : {answer}")
        
        user_input = input("Enter 'Yes' to continue calculating with the result, 'No' to start a new calculation, or 'Exit' to exit the program: ").lower()
        
        if user_input=="yes":
            num1=answer
        elif user_input=="no":
            continue_Calculation=False
            calculator()
        elif user_input=="exit":
            continue_Calculation=False
            print("Bye Bye !")
        else:
            continue_Calculation=False
            print("Invalid Input !")
            
calculator()