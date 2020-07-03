from random import shuffle

# using this as exercise to work on functions will be working towards turning this into a class. 

def dealers_deck():
    deck = []
    for suit in ['H','S','D','C']:
        for rank in ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']:
            deck.append(suit+rank)
    shuffle(deck)
    return deck 

def count_points(myCards):
    myCount = 0
    aceCount = 0 

    for i in myCards:
        if i[1] == 'T' or i[1] == 'J' or i[1] == 'Q' or i[1] == 'K':
            myCount += 10
        elif i[1] != 'A':
            myCount += int(i[1])
        else:
            aceCount += 1

        if aceCount == 1 and myCount >= 10:
            myCount += 11
        elif aceCount != 0:
            myCount += 1

    return myCount
    
def hand(myDeck):
    players_hand = []
    dealers_hand = []
    for _ in range(2):
        players_hand.append(myDeck.pop())
    for _ in range(2):
        dealers_hand.append(myDeck.pop())
    while count_points(dealers_hand) <= 17:
        dealers_hand.append(myDeck.pop())

    return players_hand, dealers_hand

# working on these feature soon 
# def take_bets():
#     

# def double_down():
#     

# def split_hand():
#     


# game logic 
 
myDeck = dealers_deck()
hands = hand(myDeck)
dealer = hands[1]
player = hands[0]

# keep track of the players score and the dealers score 
players_score = 0
dealers_score = 0

# let the player know the game is about to begin
prompt = "Welcome to wonderful game of BlackJack will you make it bigtime or find yourself in the rags. Only time will tell"
print(prompt)

while players_score <= 21:
    playerCount = count_points(player)
    dealerCount = count_points(dealer)
    print(f"The dealer has: {dealer[0]} in their hand")
    print(f"The player has: {player[0]} {player[1]} in your hand")
    print(playerCount)
    print(dealerCount)
    prompt = input('h: hit, s:stand')

    if playerCount == 21:
        print("Blackjack good one you win!")
        break
    elif playerCount > 21:
        print("To bad so sad. You lose!!!")
        break
    elif dealerCount > 21:
        print("The dealer has lost congrats your one step closer to making your dreams come true.\nDon't worry about the stress you are causing on your family!")
        break

    if prompt == "h":
        player.append(myDeck.pop())
        players_score = playerCount
        print(players_score)
    elif playerCount > dealerCount:
        print(f"you win with {playerCount} points")
        break
    else:
        print(f"Dealer wins with {dealerCount} points")
        break