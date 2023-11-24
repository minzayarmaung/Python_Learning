import random

names_string = input("Give me everybody's names , seperated by a comma. ")
names = names_string.split(", ")

print(names)

length = len(names)

print(length-1)

choose = random.randint(0,length-1)

result = names[choose]

print(f"{result} is going to pay for the meal. ")

#Aung , Kyaw , Zayar , Soe , Shoon


