import random
import art

randomNumber = random.randint(1,100)

print(randomNumber)

easyCount = 10
hardCount = 5

print(art.logo)

print("Welcome to Guessing Number Game")

print("I am thinking of a number between 1 and 100.")

level = input("Choose a Difficulty. Type 'easy' or 'hard : ").lower()

if level == "easy":
    
    while easyCount > 0:
        print(f"You have {easyCount} attempts remaining to guess the number.")
        guess = int(input("Make a Guess : "))
        
        if guess > randomNumber:
            print("Too High")
            easyCount-=1
        elif guess < randomNumber:
            print("Too Low")
            easyCount-=1
        else:
            print(f"You got it ! The answer was {randomNumber}.")
            break
            
    if easyCount == 0:
        print(f"Sorry , You Lost ! The answer was {randomNumber}")
        
elif level == "hard":
    
    while hardCount > 0:
        print(f"You have {hardCount} attempts remaining to guess the number.")
        guess = int(input("Make a Guess : "))
         
        if guess > randomNumber:
            print("Too High")
            hardCount-=1
        elif guess < randomNumber:
            print("Too Low")
            hardCount-=1
        else:
            print(f"You got it ! The answer was {randomNumber}.")
            break
    
    if hardCount == 0:
        print(f"Sorry , You Lost ! The answer was {randomNumber}.")            