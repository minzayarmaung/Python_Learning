#Functions with Output

def format_name(firstName , lastName):
    if firstName == "" or lastName == "":
        return "You didn't provide valid inputs."
    
    formatted_FName = firstName.title()
    formatted_LName = lastName.title()
    return f"Result : {formatted_FName} {formatted_LName}"

print(format_name(input("What's your First Name ? : ") , input("What's your Last Name : ")))