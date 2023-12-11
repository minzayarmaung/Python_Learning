import art
import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

print(art.logo)

bids = {}
end_the_Auction = True

def highest_bidder(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"Winner is {winner} of a bid with ${highest_bid}")
        

while end_the_Auction:
    
    name = input("What is your name?: ")
    price = int(input("What's your bid?: "))
    bids[name] = price

    def auction(name , bid):
        auction_list={}
        auction_list["name"] = name
        auction_list["bid"] = bid
        
    auction(name , price)

    result = input("Is there other user who wants to bid ? Yes or No : ").lower()
    if result == "yes":
        clear_console()
        end_the_Auction = True
    elif result == "no":
        end_the_Auction = False
        highest_bidder(bids)