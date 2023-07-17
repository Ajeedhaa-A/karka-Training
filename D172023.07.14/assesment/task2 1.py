players=[{"name":"virat_kohli","centuries":8,"half_centuries":22,"wickets":210,"hat_trick":4,"top_score":150},
        {"name":"Rohit_sharma","centuries":1,"half_centuries":35,"wickets":350,"hat_trick":7,"top_score":120},
         {"name":"Mohammed_siraj","centuries":20,"half_centuries":15,"wickets":150,"hat_trick":10,"top_score":165},
          {"name":"Ravindra_Jadeja","centuries":5,"half_centuries":31,"wickets":50,"hat_trick":8,"top_score":220},
           {"name":"Mukesh_Kumar","centuries":18,"half_centuries":29,"wickets":315,"hat_trick":9,"top_score":80} ]
count=0
def play(count):
  for player in range(len(players)):
    if (players[player]["centuries"])>10:
        count+=1
  return count
print(play(count))
print("\n")

def play2():
   for player in range(len(players)):
      if (players[player]["hat_trick"])>5:
         print(players[player]["name"])
play2()
print("\n")


def play(players):
    top=0
    for player in range (len(players)):
        if (players[player]["top_score"])>top:
            top=players[player]["top_score"]
    print(top)
play(players)
