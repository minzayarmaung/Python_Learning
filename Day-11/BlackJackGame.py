import random

print("Welcome to BlackJack Game")

def randomCard():
    randomNumbers = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    randomCard = random.choice(randomNumbers)
    return randomCard

userNum1 = randomCard()
userNum2 = randomCard()
currentScore = userNum1 + userNum2

botNum1 = randomCard()
botNum2 = randomCard()
botScore = botNum1 + botNum2

print(f"Your Card : [{userNum1} , {userNum2}]")
print(f"Current Score {currentScore}")
print(f"Computer's First Card : {botNum1}")

if currentScore == 21:
    print("You win ! You have black Jack. 😱")
elif botScore == 21 :
    print("You lose ! Opponent has Black Jack. 😱")
    

