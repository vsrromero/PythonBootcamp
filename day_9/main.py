from controller.bid_controller import calculate_auction_result
from controller.app_controller import auction
from art import welcome, logo, bid_blind

print(logo)
print(welcome)
print(bid_blind)

auction()

calculate_auction_result()
