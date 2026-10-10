players = {
    "Aman": {"score": 90,"level": 8,"coins": 2},
    "Payal": {"score":100,"level": 10,"coins":4},
    "Virat":{"score":120,"level": 12,"coins": 6},
    "Gillu": {"score":80,"level":6,"coins":1},
}

scores = []
for key,value in players.items():
    print(key,":", value)
    scores.append(value["score"])
print("Total Score:",sum(scores))  
print("Maximum Score:",max(scores)) 
print("Lowest Score:",min(scores)) 
x = len(scores)
print("Average Score:",sum(scores)/x)

for key,value in players.items():
    if value["score"] > 80:
        print(key,":",value["score"])
        
players["Aman"]["score"] = 100
players["Gillu"]["level"] = 16
players["Virat"]["score"] += 20

search_name = "Abhinay"
print(search_name in players)

to_be_removed = "Gillu"
if to_be_removed in players:
    players.pop(to_be_removed)


    