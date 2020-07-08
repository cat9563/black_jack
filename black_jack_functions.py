import random 
import sys

# using this as exercise to work on functions will be working towards turning this into a class. 

def create_deck(rank):
    """
    Creates a deck when give a list.
    """
    deck = []
    suites = ['H','S','D','C']
    for i in suites:
        for j in rank:
            deck.append(i+j)
    return deck

def Merge(dict1, dict2, dict3): 
    """
    merges 3 dictionary together 
    """
    res = {**dict1, **dict2, **dict3} 
    return res

def add_card_to_hand(hand,new_card):
    """
    adds new card to hand
    """
    new_hand = {**hand, **new_card}
    new_hand_values = new_hand.values()
    return new_hand , new_hand_values

def shuffle_deck():
    """
    Shuffles a dictionary and creates a shuffled deck. 
    """
    keys =  list(completDict.keys())
    random.shuffle(keys)

    ShuffledcompletDict = dict()
    for key in keys:
        ShuffledcompletDict.update({key:completDict[key]})
    return ShuffledcompletDict

def deal_hand(ShuffledcompletDict, n):
    """
    Deals out hand 
    """    
    # Initialize limit  
    N = n
    player = dict(list(ShuffledcompletDict.items())[0: N])
    return player

def create_dict(k, v):
    """
    Create a dictinary from a list 
    """
    card_dict = {k[i]: v[i] for i in range(len(k))} 
    return card_dict

def sum_points(hand):
    """
    Creates a sum value by evaluating the key pair in the players hand. 
    """
    values = hand.values()
    total = sum(values)
    return total, values

def error_handling():
    """
    Checks if user inserted the correct information and keeps them in a loop unitl they do. 
    """
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

def take_bets(b):
    balance = b

    while True:
        balance = b
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

def dealing_with_aces(ph):
    total_and_value  = sum_points(ph)
    total = total_and_value[0]
    value = total_and_value[1]
    new_total = []

    if total == 21:
        print("Player __ is the winner with black jack")

    if total > 21:
        for i in value:
            new_total.append(i)
        for i, num in enumerate(new_total):
            if num == 11:
                new_total[i] = 1
                new_totals = sum(new_total)
        return new_totals


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

#created a complete dictionary  
completDict = Merge(no_faceCardsDict, faceCardDict, aceCardDict)

#######################################################################

############################################################
# Provied Logic for Player and Dealer Hand                 #
############################################################

# get some player hands 
players_hand = deal_hand(shuffle_deck(), 2)
dealers_hand = deal_hand(shuffle_deck(), 2)


#account for points if value is 21 part of first check
player_points = sum_points(players_hand)
dealers_points = sum_points(dealers_hand)


# accounting for points when the value is less than 21 



#Dealing with aces
values = players_hand.values()
new_hand_total = sum(values)


# for i in values:
#     players_hand_initial_pair.append(i)
# print(players_hand_initial_pair)
# print(new_hand_total)


#Greeting
greeting = input("Welcome to Casino Cat! To start the game enter s to quit game enter q!! Have fun!!")


#Dealing with Aces
if player_points[0] == 21:
    print(f"\nTable View:\n\nPlayers Hand: {players_hand}\nPlayers Points: {player_points[0]}\nPlayer wins with Black Jack!!!")


############################################################################W
#  Get the value of a new card and append it to the values of original hand #
#############################################################################
######################################################################################################
# 1st we append the values to the list below
players_hand_initial_pair = []
for i in values:
    players_hand_initial_pair.append(i)

#find the sum of the hand 
players_total = sum(players_hand_initial_pair)

print(f"Getting the values and appending them to a list: {players_hand_initial_pair}")
 
# put in while loop 
while players_total < 21: 
# We get the values of a new card and append them to new card list 
    new_card_list = []
# define a new card 
    new_card = deal_hand(shuffle_deck(), 1)
#get the value of the new card 
    new_card_value = new_card.values()
# append the value to new card list 
    for i in new_card_value:
        new_card_list.append(i)
# append the value of new card list to the initial pair list
    players_hand_initial_pair.extend(new_card_list)
# get the players total 
    players_total = sum(players_hand_initial_pair)
    print(f"The hand total in loop is: {players_total}")
    
######################################################################################################
######################################################################################################
# Using this to display to scree the hand and the total value of the hand. 
#takes new_card variable and merges it to the existing hand
    ph_add_card = add_card_to_hand(players_hand,new_card)
#function above outputs two type of information the key value pair and just the values printing the values here 
    print(f"printing the values for ph_add_card function {ph_add_card[1]}")
######################################################################################################