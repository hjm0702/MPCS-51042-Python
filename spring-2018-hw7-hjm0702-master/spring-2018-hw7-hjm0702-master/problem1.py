from random import shuffle
from itertools import cycle
from collections import OrderedDict
from collections import Counter
from math import sqrt


'''
When 2 players and 3 owls: Prob. of Winning - 0.9772   STD - 0.00149
When 2 players and 6 owls: Prob. of Winning - 0.46365  STD - 0.00499
When 4 players and 3 owls: Prob. of Winning - 0.9581   STD - 0.002
When 4 players and 6 owls: Prob. of Winning - 0.34617  STD - 0.00476
'''

''' "p": "purple", "r": "red", "o": "orange", "b": "blue", "g": "green", "y": "yellow", "z": "sun" '''

def owl(num_players, num_owls):
    deck = ["p", "r", "o", "b", "g", "y","p", "r", "o", "b", "g", "y","p", "r", "o", "b", "g", "y",
    "p", "r", "o", "b", "g", "y","p", "r", "o", "b", "g", "y","p", "r", "o", "b", "g", "y",
    "z","z","z","z","z","z","z","z","z","z","z","z","z","z"] #Desk of the cards
    shuffle(deck)
    sun = 1 #Sun's position
    nest = 0 #The number of owls to reach the nest
    board = [["s6",0],["s5",0],["s4",0],["s3",0],["s2",0],["s1",0],
    ["b",0],["p",0],["r",0],["y",0],["g",0],
    ["b",0],["o",0],["r",0],["p",0],["y",0],
    ["g",0],["o",0],["b",0],["p",0],["r",0],
    ["g",0],["y",0],["o",0],["b",0],["p",0],
    ["r",0],["y",0],["g",0],["b",0],["o",0],
    ["r",0],["p",0],["y",0],["g",0],["b",0],
    ["o",0],["r",0],["p",0]] #[Color : The number of owl on the spot]

    '''Assign starting positions for the owls'''
    for i in range(num_owls):
        board[5-i][1] = 1

    '''Deal three cards to each player'''
    card_in_hand = [sorted([deck.pop() for card in range(3)]) for player in range(num_players) ]

    # print(board)
    # print(card_in_hand)
    # print(deck)
    turns = 0
    for turn in cycle(range(num_players)):
        turns +=1
        if sun == 14 :
            return False #Lose the game

        elif nest == num_owls:
            return True #Win the game

        else:
            '''If a player has Sun, move Sun'''
            if "z" in card_in_hand[turn]:
                sun += 1
                try :
                    card_in_hand[turn][2] = deck.pop()
                except IndexError:
                    pass
                card_in_hand[turn].sort()

            else:
                first_owl_pos = 0 #The position of the furthest owl
                max_length = 0
                card_position = 0
                '''Find the position of the furthest owl'''
                for index1, place in enumerate(board):
                    if place[1] == 1:
                        first_owl_pos = index1
                        break

                '''Find the furtherst owl can reach the nest '''
                reach_nest = False
                for index1, card in enumerate(card_in_hand[turn]):
                    if [card, 0] not in board[first_owl_pos:]:
                        reach_nest = True
                        place[1] = 0
                        try :
                            card_in_hand[turn][index1] = deck.pop()
                        except IndexError:
                            pass
                        nest = nest +1
                        break

                '''Find the best card among three of them'''
                if reach_nest == False:
                    for index2, card in enumerate(card_in_hand[turn]):
                        index3 = board[first_owl_pos:].index([card,0])
                        if index3 > max_length:
                            max_length = index3
                            card_position = index2

                    board[first_owl_pos+max_length][1] = 1
                    place[1] = 0
                    try:
                        card_in_hand[turn][card_position] = deck.pop()
                    except IndexError:
                        pass
                    card_in_hand[turn].sort()

        # print("====New Turn======")
        # print(f'Total Turn : {turns}, Turn : {turn}, Sun : {sun}, Nest : {nest}')
        # print(deck)
        # print(card_in_hand)
        # print(board)

def simulator(num_players, num_owls):
    '''Calcuate the probability of winning and standard deviation'''
    count = 0
    win_count = 0
    while count <10001:
        if owl(num_players,num_owls):
            win_count +=1
            count +=1
        else:
            count +=1
    prob = round(win_count/count,5)
    std = round(sqrt(prob*(1-prob)/count),5)
    # return prob, std

    return f'''When {num_players} players and {num_owls} owls:
Winning probability : {prob}
Standard Deviation : {std}
    '''


if __name__ == "__main__":

    # print(owl(4,6))
    print(simulator(2,3))
    print(simulator(2,6))
    print(simulator(4,3))
    print(simulator(4,6))
