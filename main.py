from replit import clear
import art

print(art.logo)
print("Welcome to the secret auction program.")

auction = {}
continue_bidding = True

while continue_bidding:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'. ")

    bidder = {}
    bidder[name] = bid
    auction.update(bidder)

    if should_continue == "yes":
        clear()
    elif should_continue == "no":
        continue_bidding = False
    else:
        print("VInvalid input! Please try again!")

#print(auction)
winner_name = max(auction, key=auction.get)
all_values = auction.values()
winner_bid = max(all_values)

print(f"The winner is {winner_name} with a bid of ${winner_bid}.")
