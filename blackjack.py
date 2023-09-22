
import random



def total (c1, c2):
    return c1 + c2
 
def greater_less_than (card_sum):
    
    if players_total > 21:
        print(f"You Lose. You have {players_total} and over 21. ")
        end_game = True
    elif players_total < 21:
        add_card = input(f"You have {player_total}. Another card? \n")
    elif player_total == 21:
        print(f"You Win. You have {card_sum} ")
        end_game = True
    
def hit ():
    hit_card = random.choice(cards)
    return hit_card

def dealer_sum():
    d_total = 0
    for d_num in d_cards:
        d_total += d_num
        
    return d_total

def player_sum():
    p_total = 0
    for p_num in p_cards:
        p_total += p_num
        
    return p_total

#Empty list for cpu and player cards
d_cards = []
p_cards = []

#cards list for both cpu and 
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

players_cards1 = random.choice(cards)
players_cards2 = random.choice(cards)

#Adding dealer cards to p_cards list
p_cards.append(players_cards1)
p_cards.append(players_cards2)

dealer_cards1 = random.choice(cards)
dealer_cards2 = random.choice(cards)

#Adding dealer cards to d_cards list
d_cards.append(dealer_cards1)
d_cards.append(dealer_cards2)

print(f"Player Cards are {players_cards1} {players_cards2} and Dealer has {dealer_cards1}")

end_game = False
while not end_game:
    #if add_card == "" or add_card == "no":
    add_card= input("Do you want a card? yes or no \n")
    player_total = player_sum()
        
    if add_card == "yes":
        p_cards.append(hit())
        player_total = player_sum()
        print(f"Player Cards are {player_total} and Dealer has {dealer_cards1}")
    elif add_card == "no":                
        dealer_total = dealer_sum()
        if dealer_total < 17:
            d_cards.append(hit())
            add_card = "no"
        elif dealer_total >= 17 and dealer_total <= 21 and player_total <=21:            
            if dealer_total > player_total:
                print(f"You lose. Dealer has {dealer_total}, Player has {player_total}")
                end_game = True
            elif dealer_total < player_total:
                print(f"You Win. Dealer has {dealer_total}, Player has {player_total}")
                end_game = True
            elif dealer_total == player_total:
                print(f"Draw. House has {dealer_total}, Player has {player_total}")
                end_game = True
        elif dealer_total > 21 and player <= 21:
            print(f"You Win. Dealer has {dealer_total}, Player has {player_total}")
            end_game = True
        elif player_total > 21 and dealer_total <= 21:
            print(f"You lose. Dealer has {dealer_total}, Player has {player_total}")
            end_game = True
        elif player_total > 21:
            print(f"You Lose. Dealer has {dealer_total}, Player has {player_total}")
            end_game = True

            
   