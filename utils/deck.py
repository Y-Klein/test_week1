import random


def create_card(rank:str,suite:str) -> dict:
    type_rank = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
    return {"rank": rank,"suite": suite,"value": type_rank.index(rank) + 2}

def create_deck() -> list[dict]:
    result = []
    type_suite = ["H","S","D","C"]
    type_rank = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
    for i in range(1,5):
        for j in range(2,15):
            result.append(create_card(type_rank[j -2],type_suite[i -1]))
    return result

def shuffle(deck:list[dict]= create_deck()) -> list[dict]:
    for i in range(1000):
        index1 = random.randint(0,51)
        index2 = random.randint(0,51)
        if index1 == index2:
            pass
        else:
            deck[index1],deck[index2] = deck[index2],deck[index1]
    return deck

def compare_cards(p1_card:dict, p2_card:dict) -> str:
    if p1_card["value"] > p2_card["value"]:
        return "p1"
    elif p1_card["value"] < p2_card["value"]:
        return "p2"
    else:
        return "WAR"