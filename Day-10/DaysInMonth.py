print("Welcome to Leap Year Calculator")

def is_leap(year):
    if year % 4 ==0:
        if year % 100 ==0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
        
def days_in_month(year , month):
    month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
    chosen_Month = month_days[month-1]
    chosen_Year = is_leap(year)
    if chosen_Year and month ==2: #February in a leap year
        return chosen_Month+1
    else:
        return chosen_Month
        
    
year = int(input("Enter the Year : "))
month = int(input("Enter the Month : "))
days = days_in_month(year , month)
print(days)