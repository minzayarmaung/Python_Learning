import random
import art

play_BlackJack = True

while play_BlackJack:
    
    def BlackJack():
        print("Welcome to Blackjack Game")
        print(art.logo)

        ace = 11

        def randomCard():
            return random.choice([11,2,3,4,5,6,7,8,9,10,10,10,10])

        def adjust_for_ace(score , num):
            if num == ace and score > 21:
                return score-10
            return score

        user_cards = [randomCard() , randomCard()]
        current_Score = sum(user_cards)

        bot_cards = [randomCard() , randomCard()]
        bot_score = sum(bot_cards)

        if current_Score == 21:
            print("You win ! You have Black Jack. 😱")
        elif bot_score == 21:
            print("You Lose ! Opponent has Black Jack 😱")

        while True:
            print(f"Your Cards : {user_cards} , current score : {current_Score}")
            print(f"Computer's first Card : {bot_cards[0]}")
            
            user_decision = input("Type 'y' to get another card , type 'n' to pass : ")
            
            if user_decision == "y":
                new_card = randomCard()
                user_cards.append(new_card)
                current_Score += new_card
                current_Score = adjust_for_ace(current_Score , new_card)
                
                if current_Score>21:
                    print(f"Your final hand : {user_cards}, final score : {current_Score}")
                    print(f"Computer's Final Hand : {bot_cards} final score : {bot_score}")         
                    print("You went Over. You Lose 🥲")
                    break
            
            else:
                while bot_score < 17:
                    new_bot_card = randomCard()
                    bot_cards.append(new_bot_card)
                    bot_score += new_bot_card
                    bot_score = adjust_for_ace(bot_score , new_bot_card)
            
                print(f"Your Final Hand : {user_cards} , final Score : {current_Score}")
                print(f"Computer's Final Hand : {bot_cards}, final Score : {bot_score}")
                
                if bot_score > 21:
                    print("Opponent Went Over. You win ! 😃")
                elif current_Score > bot_score:
                    print("You Win ! 😁")
                elif current_Score < bot_score:
                    print("You Lose ! 🥺")
                else:
                    print("It's a draw 🥲")
                break
    
    BlackJack()
    
    continue_Game = input("Type 'yes' to PLay again , type 'no' to Exit : ").lower()
    if continue_Game != "yes":
        play_BlackJack = False
        print("Bye Bye 👋")
   