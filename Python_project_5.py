'''                 <-----------------My attempt------------->                  '''
'''  Silent Auction Program---------> '''
# import os
# yes=False
# data={}
# while not yes:
#     name=input("What is your name?")
#     bid=int(input("What is your bid?"))
#     data[name]=bid
#     max_bid=data[name]
#     winner=name
#     # print(max_bid)
#     print(data)
#     choice=input("Are there any other bidders? Type 'yes' or 'no'.")
#     if choice=='yes':
#         os.system("cls")
#     else:
#        max_bid=data[name]
#        yes=True
# for i in data:
#     if data[i]>max_bid:
#         max_bid=data[i]
#         winner=i
# print(f'The winner is {winner} with a bid of {max_bid}.')


'''         <-------------------Ma'am solution------------------->                        '''
import os
def find_winner(bidder_details):   #{jenny: 10000, Ram 30000, Shyam:5000}
    
    highest_bid=0   #30000
    for bidder in bidder_details:   #jenny
        bidding_price=bidder_details[bidder]    #10000
        if bidding_price>highest_bid:
            highest_bid=bidding_price
            winner=bidder
    print(f'Here is the list ofall the bidders:{bidder_details}')
    print(f'The winner is {winner} with a bid price of {highest_bid}')

bidder_data={}
end_of_bidding=False
while not end_of_bidding:
    name=input("What is your name:")
    price=int(input("What is your bid?"))
    bidder_data[name]=price
    more_bidders=input("Are there more bidders? Type 'yes' or 'no' :").lower()
    if more_bidders=='no':
        end_of_bidding=True
        find_winner(bidder_data)
        # print(bidder_data)

    elif more_bidders=='yes':
        os.system("cls")