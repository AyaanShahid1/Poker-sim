import random
from itertools import combinations
from collections import Counter
import pandas as pd
import os

D={"H":"Hearts", "D": "Diamonds", "C": "Clubs", "S": "Spades", "K": "King", "J": "Jack", "Q": "Queen", "A": "Ace"}

class Card:

    suits = ["H","D","C","S"]
    ranks = [str(n) for n in range(2, 11)] + ["J", "Q", "K", "A"]
    


    def __init__(self, Value, Suit):
        self.Value = Value
        self.Suit = Suit

    def __repr__(self):
        return f"{self.Value}{self.Suit}"

class Deck: 
    def __init__(self):
        self.cards = [Card(rank, suit) for suit in Card.suits for rank in Card.ranks]
    
    def __repr__(self):
        return f"{self.cards}"
    
    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, num):
        dealt = self.cards[:num]
        self.cards = self.cards[num:]
        return dealt
    
    def show(self, label, cards):
         return f"{label}: {', '.join(f'{D.get(card.Value, card.Value)} of {D.get(card.Suit, card.Suit)}' for card in cards)}"

class Player:
    def __init__(self, name, hand=None, score = None, best_hand = None):
        self.name = name
        self.hand = hand if hand else []
        self.score = score if score is not None else 0
        self.best_hand = best_hand if best_hand is None else []

    def show_hand(self):
        return f"{self.name}'s hand: {', '.join(f'{D.get(card.Value, card.Value)} of {D.get(card.Suit, card.Suit)}' for card in self.hand)}"
    
def play(player_count, show = True): # game function
    deck = Deck()
    deck.shuffle()

    players = [Player(f"Player {i+1}", deck.deal(2)) for i in range(player_count)] # num of players

    q = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,"8": 8, "9": 9, "10": 10,"J": 11, "Q": 12, "K": 13, "A": 14}
    hand_rankings = {"High Card": 1,"One Pair": 2,"Two Pair": 3,"Three of a Kind": 4,"Straight": 5,"Flush": 6,"Full House": 7,"Four of a Kind": 8,"Straight Flush": 9,
                     "Royal Flush": 10}
    rank_to_name = {v: k for k, v in hand_rankings.items()} # reverse of above

    Flop = deck.deal(3) # community cards
    Turn = deck.deal(1)
    River = deck.deal(1)
    board1 = Flop + Turn
    full_board = board1 + River
    if show:
        for player in players:
            print(player.show_hand())
            print()
        filter1 = df.loc[df["player1 hand"] == ",".join(str(c) for c in players[0].hand)]
        filter2 = df.loc[df["player2 hand"] == ",".join(str(c) for c in players[1].hand)]
        if not filter1.empty:
            print( f"player1 win %: {(filter1["player1 wins"].sum()) / (filter1["total games"].sum()):.2%}")
            print()
        else:
            print(f"player1 win %: Insufficiant games in database")
            print()

        if not filter2.empty:
            print( f"player2 win %: {(filter2["player2 wins"].sum()) / (filter2["total games"].sum()):.2%}")
            print()
        else:
            print(f"player2 win % : Insufficiant games in database")
            print()


        filter3 = filter1.loc[filter1["player2 hand"] == ",".join(str(c) for c in players[1].hand)]
        if not filter3.empty: 
            print(f"player1 win % vs player 2 hand : {(filter3["player1 wins"].sum()) / filter3["total games"].sum():.2%}")
            print()
            print(f"player2 win % vs player 1 hand : {(filter3["player2 wins"].sum()) / filter3["total games"].sum():.2%}")
            print()
        else:
            print(f"player1 win % vs player 2 hand : insufficiant games in database")
            print()
            print(f"player2 win % vs player 1 hand : insufficiant games in database")
            print()

        
        input("action : ")
        print()
        print(deck.show("Flop",Flop))
        print()

        filter4 = filter3.loc[filter3["flop"] == str(Flop)]
        if not filter4.empty:
            print(f"player1 win % vs player 2 hand with flop {str(Flop)} : {(filter4["player1 wins"].sum()) / filter4["total gamess"].sum():.2%}")
            print()
            print(f"player2 win % vs player 1 hand with flop {str(Flop)} : {(filter4["player2 wins"].sum()) / filter4["total games"].sum():.2%}")
            print()
        else:
            print(f"player1 win % vs player 2 hand with flop {str(Flop)} : insufficiant games in database")
            print()
            print(f"player2 win % vs player 1 hand with flop {str(Flop)} : insufficiant games in database")
            print()

        input("action : ")
        print()
        print(deck.show("Turn",Turn))
        print()

        filter5 = filter4.loc[filter4["turn"] == str(Turn)]
        if not filter5.empty:
            print(f"player1 win % vs player 2 hand with board {str(board1)} : {(filter5["player1 wins"].sum()) / filter5["total games"].sum():.2%}")
            print()
            print(f"player2 win % vs player 1 hand with board {str(board1)} : {(filter5["player2 wins"].sum()) / filter5["total games"].sum():.2%}")
            print()
        else:
            print(f"player1 win % vs player 2 hand with board {str(board1)} : insufficiant games in database")
            print()
            print(f"player2 win % vs player 1 hand with board {str(board1)} : insufficiant games in database")
            print()

        input("action : ")
        print()
        print(deck.show("River",River))
        print()

        filter6 = filter5.loc[filter5["river"] == str(River)]
        if not filter5.empty:
            print(f"player1 win % vs player 2 hand with board {str(full_board)} : {(filter6["player1 wins"].sum()) / filter6["total games"].sum():.2%}")
            print()
            print(f"player2 win % vs player 1 hand with board {str(full_board)} : {(filter6["player2 wins"].sum()) / filter6["total games"].sum():.2%}")
            print()
        else:
            print(f"player1 win % vs player 2 hand with board {str(full_board)} : insufficiant games in database")
            print()
            print(f"player2 win % vs player 1 hand with board {str(full_board)} : insufficiant games in database")
            print()
        
        print(deck.show("full_board",full_board))
        print()
        input("action : ")
        print()


    for player in players: # loop to check hands

        full_hand = player.hand + Flop + Turn + River
        all_hands = combinations(full_hand, 5)
        best = max(evaluate(hands) for hands in all_hands)
        player.score = best
        values = [q.get(card.Value) for card in full_hand]
        suits = [card.Suit for card in full_hand]
        player.best_hand = best
        if show:
            print(f"{player.name}'s best hand: {rank_to_name[best[0]]} {best}")
            print()
    
    max_score = max(p.score for p in players)
    winners = [p for p in players if p.score == max_score]
    p1_win = 1 if players[0] in winners else 0
    p2_win = 1 if players[1] in winners else 0
    total_games = 1

    data = {"player1 hand" :",".join(str(c) for c in players[0].hand),"player2 hand" : ",".join(str(c) for c in players[1].hand),
                "flop" : str(Flop), "turn" : str(Turn[0]), "river" : str(River[0]), "player1 wins" : p1_win, "player2 wins" : p2_win, "total games" : total_games}
    if show:
        if len(winners) > 1:
            print(f"\n🏆 Tie between: {', '.join(w.name for w in winners)} with {rank_to_name[winners[0].score[0]]} {winners[0].score[1:]}")
        else:
            print(f"\n🏆 Winner: {winners[0].name} with {rank_to_name[winners[0].score[0]]} {winners[0].score[1:]}")


    return data
            
def evaluate(cards): # hand ranker
    q = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,"8": 8, "9": 9, "10": 10,"J": 11, "Q": 12, "K": 13, "A": 14}
    values = sorted([q[card.Value] for card in cards], reverse=True)
    suits = [card.Suit for card in cards]
    counts = Counter(values)
    flush = len(set(suits)) == 1
    Unique_values = sorted(set(values), reverse = True)
    

    is_straight = False
    straight_high = 0
    if len(Unique_values) >= 5:
        # Check for normal straight
        for i in range(len(Unique_values) - 4):
            if Unique_values[i] - Unique_values[i+4] == 4:
                is_straight = True
                straight_high = Unique_values[i]
                break
        # Check for wheel
        if not is_straight and set(values).issuperset({14, 2, 3, 4, 5}):
            is_straight = True
            straight_high = 5
    
    if flush and is_straight and max(values) == 14:
        return (10,)
    
    # Straight Flush
    elif flush and is_straight:
        return (9, straight_high,)
    
    # Four of a Kind
    elif 4 in counts.values():
        quad = next(v for v, cnt in counts.items() if cnt == 4)
        kicker = max(v for v in values if v != quad)
        return (8, quad, kicker)
    
    # Full House
    elif sorted(counts.values(), reverse=True)[:2] == [3, 2] or list(counts.values()).count(3) >= 2:
        trio = max(v for v, c in counts.items() if c == 3)
        pair = max(v for v, c in counts.items() if c >= 2 and v != trio)
        return (7, trio, pair)
    
    # Flush
    elif flush:
        return (6, *values[:5]) 
    
    # Straight
    elif is_straight:
        return (5, straight_high,)
    
    # Three of a Kind
    elif 3 in counts.values():
        trio = next(v for v, cnt in counts.items() if cnt == 3)
        kickers = sorted([v for v in values if v != trio], reverse=True)[:2]
        return (4, trio, *kickers,)
    
    # Two Pair
    elif list(counts.values()).count(2) >= 2:
        pairs = sorted([v for v, cnt in counts.items() if cnt == 2], reverse=True)[:2]
        kicker = max(v for v in values if v not in pairs)
        return (3, *pairs, kicker,)
    
    # One Pair
    elif 2 in counts.values():
        pair = next(v for v, cnt in counts.items() if cnt == 2)
        kickers = sorted([v for v in values if v != pair], reverse=True)[:3]
        return (2, pair, *kickers,)
    
    # High Card
    else:
        return (1, *values[:5])
    

data = "poker_data.csv"

if os.path.exists(data) and os.path.getsize(data) > 2:
    df = pd.read_csv(data)
    all_records_2players = df.to_dict(orient = "records")
    keys = set(
        tuple(sorted(row["player1 hand"].replace(",", "").replace(" ", "").split()) + sorted(row["player2 hand"].replace(",", "").replace(" ", "").split()) +
              sorted(row["flop"].strip("[]").replace(", ", " ").split()) + row["turn"].split() + row["river"].split())
        for row in all_records_2players
    )
else: 
    all_records_2players = []
    keys = set()

                                 ###### ------------ DATA CREATOR DO NOT USE AGAIN OR PC WILL EXPLODE  ------------- ############
#for i in range(1):
    #records = play(2, show = False)
    #player1_hand = tuple(sorted(records["player1 hand"].replace(",", "").replace(" ", "").split()))
    #player2_hand = tuple(sorted(records["player2 hand"].replace(",", "").replace(" ", "").split()))
    #flop = tuple(sorted(records["flop"].strip("[]").replace(", ", " ").split()))
    #turn = tuple(records["turn"].split())
    #river = tuple(records["river"].split())
    #game_key = (player1_hand + player2_hand + flop + turn + river)

    #if game_key not in keys:
        #keys.add(game_key)
        #all_records_2players.append(records)

df = pd.DataFrame(all_records_2players)
df.to_csv(data, index = False)
play(2)