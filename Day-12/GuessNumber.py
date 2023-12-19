import random
import art

randomNumber = random.randint(1,100)

def countNumber(level):
    if level == "easy":
        return 10
    else:
        return 5
    

print(art.logo)
print(f"Hint : {randomNumber}")
print("Welcome to Guessing Number Game !")
print("I am thinking of a Number between 1 and 100.")
level = input("Choose the Level : Type 'Easy' or 'Hard' : ").lower()
count = countNumber(level)

while count > 0:
    print(f"You have {count} attempts remaining to guess.")
    guess = int(input("Guess a Number : "))
    
    if guess > randomNumber:
        print("Too High")
    elif guess < randomNumber:
        print("Too Low")
    else:
        print(f"You got it ! The Number was {randomNumber}.")
        count=0
        
    count-=1
    
if count==0:
    print(f"You Lose ! The Number was {randomNumber}")