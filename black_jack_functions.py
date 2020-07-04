from random import shuffle
import sys

# using this as exercise to work on functions will be working towards turning this into a class. 

def create_deck(rank):
    deck = []
    suites = ['H','S','D','C']
    for i in suites:
        for j in rank:
            deck.append(i+j)
    return deck

def Merge(dict1, dict2, dict3): 
    res = {**dict1, **dict2, **dict3} 
    return res

#######################
# creates a list of key value pairs in a dictionary and set of tuples 
# will probably continue with using tuples out of curiousity. 
#######################
no_faceCards = create_deck(['2', '3', '4', '5', '6', '7', '8', '9', '10'])
faceCards = create_deck(['J', 'Q', 'K'])
aceCards = create_deck(['A'])

# this allows for the value to be numeric and I can use sum to add up the value of the cards
no_faceValues = list(range(2,11)) * 4
faceCarValues = [10,10,10] * 4
# will need logic for handling aces 
aceValues = [11] * 4

### create function to avoid repeat code here 
no_faceCardsDict = {no_faceCards[i]: no_faceValues[i] for i in range(len(no_faceCards))} 
faceCardDict = {faceCards[i]: faceCarValues[i] for i in range(len(faceCards))} 
aceCardDict = {aceCards[i]: aceValues[i] for i in range(len(aceCards))} 

#created a dict then converts to a list of tuples  
completDict = Merge(no_faceCardsDict, faceCardDict, aceCardDict)
completeTuple = list(completDict.items())
deck = shuffle(completeTuple)


# change point logic next 
# def count_points(myCards):
#     myCount = 0
#     aceCount = 0 

#     for i in myCards:
#         if i[1] == 'T' or i[1] == 'J' or i[1] == 'Q' or i[1] == 'K':
#             myCount += 10
#         elif i[1] != 'A':
#             myCount += int(i[1])
#         else:
#             aceCount += 1

#         if aceCount == 1 and myCount >= 10:
#             myCount += 11
#         elif aceCount != 0:
#             myCount += 1

#     return myCount

# Need to update hand function as well
# 
# player = []
# for _ in range(2):
#     player.append(completeTuple.pop())
#      
# def hand(myDeck):
#     players_hand = []
#     dealers_hand = []
#     for _ in range(2):
#         players_hand.append(myDeck.pop())
#     for _ in range(2):
#         dealers_hand.append(myDeck.pop())
#     while count_points(dealers_hand) <= 17:
#         dealers_hand.append(myDeck.pop())

#     return players_hand, dealers_hand


def error_handling():
    betting_rules = ("House Rules\nBets must be greater than $5\nNo change excepetd only dollars y'all!\n")
    print(betting_rules)
    while True:
        num = input("How much woud you like to bet: ")
        try:
            val = int(num)
            return val
        except ValueError:
            print("Less talk more give.\n")
        print(val)

def take_bets():
    balance = 200 

    while True:
        balance = 200
        users_bet = error_handling()
        if users_bet > balance:
            print("you don't have that much in your account.\nYou might want to head out to the pawnshop or work the corner!\n") 
        elif users_bet < 5:
            print( "common man you don't have $5, seriously you need help!\nWe only take bets greater than $5!!\n")
        else:
            print("GOOD LUCK CHAMP!")
            print(f"Thanks for your donation of ${users_bet}. The house appreciates you.\n")
        return users_bet

def double_down(double_down):
    bet = double_down
    return bet * 2

#I changed deck logic will need to check through and make need changes    
# def split_hand(prompt):
#     myDeck = dealers_deck()
#     split_hand = hand(myDeck)
#     player = split_hand[0]

#     split_hand1 = [player[0]]
#     split_hand2 = [player[1]]

#     if prompt == "S":
#         split_hand1.append(myDeck.pop())
#         split_hand2.append(myDeck.pop())
#     else:
#         pass
#     return split_hand1, split_hand2

# game logic 

###########################
# game logic is really bugy changed deck logic need to update this section after completing functions

###########################
 
# myDeck = dealers_deck()
# hands = hand(myDeck)
# dealer = hands[1]
# player = hands[0]

# # keep track of the players score and the dealers score 
# players_score = 0
# dealers_score = 0

# # let the player know the game is about to begin
# prompt = "Welcome to wonderful game of BlackJack will you make it bigtime or find yourself in the rags. Only time will tell"
# print(prompt)

# while players_score <= 21:
#     playerCount = count_points(player)
#     dealerCount = count_points(dealer)
#     print(f"The dealer has: {dealer[0]} in their hand")
#     print(f"The player has: {player[0]} {player[1]} in your hand")
#     print(playerCount)
#     print(dealerCount)
#     prompt = input('h: hit, s:stand')

#     if playerCount == 21:
#         print("Blackjack good one you win!")
#         break
#     elif playerCount > 21:
#         print("To bad so sad. You lose!!!")
#         break
#     elif dealerCount > 21:
#         print("The dealer has lost congrats your one step closer to making your dreams come true.\nDon't worry about the stress you are causing on your family!")
#         break

#     if prompt == "h":
#         player.append(myDeck.pop())
#         players_score = playerCount
#         print(players_score)
#     elif playerCount > dealerCount:
#         print(f"you win with {playerCount} points")
#         break
#     else:
#         print(f"Dealer wins with {dealerCount} points")
#         break