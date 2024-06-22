###統計116
###鄭雅云 H24126078


import random
ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
suits = ['S', 'H', 'D', 'C'] ###Spades Heart Diamond Club
card_values = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13}

def createShuffledDeck(): ###這是建立一副牌
    deck = []
    for s in suits:
        for r in ranks:
            deck.append(s+r)  ##牌長這樣：SA, H2
    random.shuffle(deck)
    return deck

def drawCard(deck, num): ###這是洗牌
    cards = []
    for i in range(num):
        card = deck.pop(0)
        cards.append(card)
    return cards

def calculus_the_value(hand):
    total_value = 0
    num_aces = 0
    for card in hand:
        the_value = card[1:]
        if the_value == "A":
            num_aces += 1
        elif the_value in ["J", "Q", "K"]:
            total_value += 10
        else:
            total_value += int(the_value)

    # 根據目前的總值決定 A 的值是 1 還是 11
    for _ in range(num_aces):
        if total_value + 11 <= 21:
            total_value += 11
        else:
            total_value += 1

    return total_value


##抽一張牌：drawCard(deck, 1)
##剩餘牌數：len(deck)

deck = createShuffledDeck()
beginofdealer = drawCard(deck, 2)
beginofplayer = drawCard(deck, 2)
cardvalue_of_dealer = calculus_the_value(beginofdealer)
cardvalue_of_player = calculus_the_value(beginofplayer)

if_next_game = True

while if_next_game:
    while cardvalue_of_player < 21:
        print("\nYour current value is %d" %cardvalue_of_player)
        print("with the hand: ", beginofplayer)

        whether =input("\nHit or Stay? (Hit = 1, Stay = 0):")
        if whether == "0":
            break
        if whether == "1":
            newcard = deck.pop(0)
            beginofplayer.append(newcard)
            print()
            print("You draw:", newcard)
            cardvalue_of_player = calculus_the_value(beginofplayer)

    if cardvalue_of_player > 21:
        print("Bust!(>21)")
    if cardvalue_of_player == 21:
        print("Your current value is", 21)
        print("With the hand",beginofplayer)
        print("Black jack")

    print()
    print("---Dealer---")

    print("\nDealer's current value is", cardvalue_of_dealer)
    print("With the hand", beginofdealer)
    while cardvalue_of_dealer < 21:
        while cardvalue_of_dealer <= 17:
            third_card = deck.pop(0)
            print("\nDealer draw", third_card)
            beginofdealer.append(third_card)
            cardvalue_of_dealer = calculus_the_value(beginofdealer)
            print("\nDealer's current value is", cardvalue_of_dealer)
            print("With the hand", beginofdealer)
        if cardvalue_of_dealer > 17:
            break

    if cardvalue_of_dealer == 21:
        print("\nDealer's current value is", 21)
        print("With the hand", beginofdealer)
        print("\nBlack jack")
    elif cardvalue_of_dealer > 21:
        print("\nBust!(>21)")

    if cardvalue_of_player <= 21 and cardvalue_of_dealer <= 21:
        if cardvalue_of_player > cardvalue_of_dealer:
            print("***You beat the dealer!***")
        elif cardvalue_of_player < cardvalue_of_dealer:
            print("***Dealer wins***")
        elif cardvalue_of_player == cardvalue_of_dealer:
            print("***You tied the dealer, nobody wins***")
    elif cardvalue_of_player > 21 and cardvalue_of_dealer > 21:
        print("***You tied the dealer, nobody wins***")
    elif cardvalue_of_player <= 21 and cardvalue_of_dealer > 21:
        print("***You beat the dealer!***")
    elif cardvalue_of_player > 21 and cardvalue_of_dealer <= 21:
        print("***Dealer wins***")  

    yes_or_no = input("Want to play again?(y/n):")
    if yes_or_no == "y":
        deck = createShuffledDeck()
        beginofdealer = []
        beginofplayer = []
        cardvalue_of_dealer = 0
        cardvalue_of_player = 0

        deck = createShuffledDeck()
        beginofdealer = drawCard(deck, 2)
        beginofplayer = drawCard(deck, 2)
        cardvalue_of_dealer = calculus_the_value(beginofdealer)
        cardvalue_of_player = calculus_the_value(beginofplayer)
        if_next_game = True
        print()
        print("-------------------------------------")
        print()
    if yes_or_no == "n":
        if_next_game = False