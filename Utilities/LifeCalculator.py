age = int(input("What is your Current Age?\n"))

totalDays = int(90*365)
totalWeeks = int(90*52)
totalMonths = int(90*12)

remainDays = int(age * 365)
remainWeeks = int(age * 52)
remainMonths = int(age * 12)

remainTotalDays = totalDays - remainDays
remainTotalWeeks = totalWeeks - remainWeeks
remainTotalMonths = totalMonths - remainMonths

print(f"You have {remainTotalDays} Days  , {remainTotalWeeks}  weeks and {remainTotalMonths} months left")