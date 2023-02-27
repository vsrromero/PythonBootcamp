auction_list = []

def calculate_auction_result():
    winner = ''
    winning_bid = 0
    for bid in auction_list:
        if bid['bid'] > winning_bid:
            winner = bid['name']
            winning_bid = bid['bid']
    print(f'The winner of the auction is {winner.upper()} with a bid of ${winning_bid}.')

def add_bid(new_bidder, bid):
    new_bid = {}
    new_bid['name'] = new_bidder
    new_bid['bid'] = bid
    auction_list.append(new_bid)