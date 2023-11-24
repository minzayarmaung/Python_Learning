import random

print("Toss a Coin and Let's see the Result ! ")

random_coin = random.randint(1,2)

if random_coin == 1:
    print("It is a Head")
elif random_coin == 2:
    print("It is a Tail")