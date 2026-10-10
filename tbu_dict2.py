players = {
    "Aman": {"score": 750,"level":16,"coins": 75},
    "Virat":{"score": 500,"level":10,"coins": 50},
    "Rohit":{"score": 800,"level":20,"coins":80}
}

Scores = []
Coins = []
Level = []
for key,value in players.items():
   print(key,value["score"])
   Scores.append(value["score"])
   Coins.append(value["coins"])
   Level.append(value["level"])
   
print("Total Score:",sum(Scores))
print("Highest Score:",max(Scores))
print("Minimum Score:",min(Scores))
print("Total Coins :",sum(Coins))
for key,value in players.items():
    if value["level"] >= 20:
        print(key,":",value["level"])


   
   
 