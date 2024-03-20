from logo import logo

print(logo)

bidders = {}
more_players = True

while more_players:
    name = input("What is your name? ")
    bid = int(input("What is your bid? "))
    bidders[name] = bid
    still_bids = input("IS there any more bidders? y or n? ").lower()
    if still_bids == "n":
        more_players = False


def find_bidder(dict1):
    v = list(dict1.values())
    k = list(dict1.keys())
    print(f"{k[v.index(max(v))]} has highest bid : {v}")


find_bidder(bidders)
