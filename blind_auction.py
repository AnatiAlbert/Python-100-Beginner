from blind_auction_art import logo
print(logo)

auction_stop = False

bid_group = {}

def high_bid(bid_sample):
    highest = 0
    winner = ""
    for bids in bid_sample:
        bid_amount = bid_sample[bids]
        if bid_amount > highest:
            highest = bid_amount
            winner = bids

    print(f"{winner} wins with the bid amount of ${highest}")

while not auction_stop:
    name = input("Enter the bidder's name?\n")
    bid_price = int(input("How much will you bid?\n$"))

    bid_group[name] = bid_price

    other_bid = input("Are there other bidders, 'yes' or 'no'?\n").lower()

    if other_bid == "yes":
        print("\n" * 3)
    elif other_bid == "no":
        high_bid(bid_group)
        auction_stop = True
