import random
import art
import game_data

'''
|| About this program ||

This program is called "Higher or Lower". You can search this on Google and play the game.
I recommend to play. So that you will get it how does this program works

|| How this game works ? ||

(1) First , the program will show you two celebrities around the world.
    You have to guess their insta follower numbers. The numbers could be wrong but "Hey , this is just a game"
(2) If you have guessed right , then the program will give u another one to guess with your recent correct one
(3) If you guessed it wrong , the program will then stop and show ur scores.

|| How this game was programmed ? ||

(1) First we initializes get_random_person() function to generate a random number from the dictionary from 
    the game_data_py. 
(2)  Then we are getting the infos about the celebrities from the dictionary and assign each value into
    their respective variables.
(3)  Then we are doing some logical , comparing the amount of followers .
(4)  The game will stop immediately if u have guessed wrong.
'''


def get_random_person():
    return random.choice(game_data.data)


def gameplay():
    count = 0
    print(art.logo)
    personA = get_random_person()
    personB = get_random_person()

    while True:

        name = personA['name']
        description = personA['description']
        country = personA['country']
        followersA = int(personA['follower_count'])

        name1 = personB['name']
        description1 = personB['description']
        country1 = personB['country']
        followersB = int(personB['follower_count'])

        print(f"Compare A : {name} , {description} , from {country}")
        print(art.vs)
        print(f"Compare B : {name1} , {description1} , from {country1}")

        choose = input("Who has more followers? Type 'A' or 'B' : ").upper()

        if (choose == 'A' and followersA > followersB) or (choose == 'B' and followersB > followersA):
            count += 1
            print(f"You're right ! Current Score : {count}")

            if followersA > followersB:
                personB = get_random_person()
            else:
                personB = personB
            if followersB > followersA:
                personA = get_random_person()
            else:
                personA = personA
        else:
            print(f"Sorry , that's wrong. Final score : {count}")
            break


gameplay()
