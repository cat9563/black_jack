import random 
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

def shuffle_deck():
    keys =  list(completDict.keys())
    random.shuffle(keys)

    ShuffledcompletDict = dict()
    for key in keys:
        ShuffledcompletDict.update({key:completDict[key]})
    return ShuffledcompletDict

def deal_hand(ShuffledcompletDict):    
    # Initialize limit  
    N = 2
    player = dict(list(ShuffledcompletDict.items())[0: N])
    dealer = dict(list(ShuffledcompletDict.items())[0: N])
    return player, dealer 

def create_dict(k, v):
    card_dict = {k[i]: v[i] for i in range(len(k))} 
    return card_dict

def sum_points(hand):
    values = hand.values()
    total = sum(values)
    return total

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


#######################################################################
# Creates a list of key value pairs in a dictionary                   #
#######################################################################

no_faceCards = create_deck(['2', '3', '4', '5', '6', '7', '8', '9', '10'])
faceCards = create_deck(['J', 'Q', 'K'])
aceCards = create_deck(['A'])

no_faceValues = list(range(2,11)) * 4
faceCarValues = [10,10,10] * 4 
aceValues = [11] * 4

no_faceCardsDict = create_dict(no_faceCards, no_faceValues)
faceCardDict = create_dict(faceCards, faceCarValues)
aceCardDict = create_dict(aceCards, aceValues)

#created a dict then converts to a list of tuples  
completDict = Merge(no_faceCardsDict, faceCardDict, aceCardDict)
completeTuple = list(completDict.items())

#######################################################################
