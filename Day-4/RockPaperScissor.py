import random

# Rock Paper Scissors ASCII Art

# Rock

rock_shape = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper_shape = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissor_shape = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""


print("Welcome to Rock Paper Scissor Game !")

bot = random.randint(0,2)

choose = input("Choose Rock , Paper , Scissor ")
choose_lowercase = choose.lower()

if choose_lowercase == "rock" and bot == 0:
    print("You choose : " , rock_shape)
    print("Bot choose : " , rock_shape)
    print("Draw")
    
elif choose_lowercase == "paper" and bot == 1:  
    print("You choose : " , paper_shape) 
    print("Bot choose : " , paper_shape)
    print("Draw")   

elif choose_lowercase == "scissor" and bot == 2:  
    print("You choose : " , scissor_shape) 
    print("Bot choose : " , scissor_shape)
    print("Draw !")     

elif choose_lowercase == "rock" and bot == 1:
    print("You choose : " , rock_shape)
    print("Bot choose : " , paper_shape)
    print("You Lose !")

elif choose_lowercase == "rock" and bot == 2:
    print("You choose : " , rock_shape)
    print("Bot choose : " , scissor_shape)
    print("You Win !")
    
elif choose_lowercase == "paper" and bot == 0:
    print("You choose : " , paper_shape)
    print("Bot choose : " , rock_shape)
    print("You Win !")

elif choose_lowercase == "paper" and bot == 2:
    print("You choose : " , paper_shape)
    print("Bot choose : " , scissor_shape)
    print("You Lose !")
    
elif choose_lowercase == "scissor" and bot == 0:
    print("You choose : " , scissor_shape)
    print("Bot choose : " , rock_shape)
    print("You Lose !")

elif choose_lowercase == "scissor" and bot == 1:
    print("You choose : " , scissor_shape)
    print("Bot choose : " , paper_shape)
    print("You Win !")