from game_logic.game import *
if __name__=="__main__":

     s = init_game()
     p1 = create_player(input("enter your name") )
     p2 = create_player("")
     p1["hand"] = s["player_1"]
     p2["hand"] = s["player_2"]

     while len(p2["hand"]) > 0:
          play_round(p1,p2)
          input()
     print("************🎉🎉🎉**************")
     if len(p1["won_pile"]) > len(p2["won_pile"]):
          print(f"the big winner is {p1["name"]}")
     elif len(p1["won_pile"]) < len(p2["won_pile"]):
          print(f"the big winner is {p2["name"]}")
     else:
          print("teko")

