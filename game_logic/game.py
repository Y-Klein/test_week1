from utils.deck import shuffle,compare_cards
def create_player(name:str ) -> dict:
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

def play_round(p1:dict,p2:dict):
    result_win = compare_cards(p1["hand"][0], p2["hand"][0])
    print(f"{p1["name"]} cerd is:{p1["hand"][0]}")
    print(f"{p2["name"]} cerd is:{p2["hand"][0]}")

    if result_win == "p1":
        p1["won_pile"].append(p1["hand"][0])
        p1["won_pile"].append(p2["hand"][0])
        print(f"{p1["name"]} is win")
    elif result_win == "p2":
        p2["won_pile"].append(p1["hand"][0])
        p2["won_pile"].append(p2["hand"][0])
        print(f"{p2["name"]} is win ")
    elif result_win == "WAR":
        print("WAR")
    p1["hand"] = p1["hand"][1:]
    p2["hand"] = p2["hand"][1:]
    print(f"nikod of {p1["name"]} is :{int(len(p1["won_pile"]) /2)}")
    print(f"nikod of {p2["name"]} is :{int(len(p2["won_pile"])/2)}")

