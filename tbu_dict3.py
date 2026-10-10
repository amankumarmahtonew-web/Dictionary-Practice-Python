player = {
    "name": "Aman",
    "score": 850,
    "level": 25,
    "coins": 1600
}
print(player["name"])
print(player["score"])
player["level"] = 20
player["rank"] = "Conqueror"
player["gold"] = "Payal"

print("coins" in player)

print(player.keys())
print(player.values())

for key,value in player.items():
    print(key,":",value)
    
player.pop("coins")    

print(player)