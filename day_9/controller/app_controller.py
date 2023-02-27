from bid_controller import add_bid
import os

def auction():
    auction_running = True
    while auction_running:

        bidder = input('What is your name? ')
        bid = round(float(input('What is your bid? $')), 2)

        add_bid(bidder, bid)

        more_bids = input('Are there any other bidders? Type "yes" or "no": ')

        if more_bids == 'no':
            auction_running = False
            
        clear_screen = 'cls' if os.name == 'nt' else 'clear'
        os.system(clear_screen)