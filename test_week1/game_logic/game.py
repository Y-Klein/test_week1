from utils.deck import *
def create_player(name:str = input("enter your name") ) -> dict:
    if name == "":
        name = "AI"
    hand = []
    won_pile = []
    return {"name":name,"hand":hand,"won_pile":won_pile}

def init_game()->dict:
    deck = shuffle()
    player_1 = deck[:26]
    player_2 = deck[26:]

    return {"deck":deck,"player_1":player_1,"player_2":player_2}

def play_round(p1:dict,p2:dict):#משחק סיבוב אחד
    result_win = compare_cards(p1["hand"][0], p2["hand"][0])
    if result_win == "p1":
        p1["won_pile"].append(p1["hand"][0], p2["hand"][0])
    elif result_win == "p2":
        p2["won_pile"].append(p1["hand"][0], p2["hand"][0])
    p1["hand"] = p1["hand"][1:]
    p2["hand"] = p2["hand"][1:]
