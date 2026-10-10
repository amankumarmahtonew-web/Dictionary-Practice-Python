
Aman = {
    "name": "Aman",
    "health": "Decent",
    "age": 15,
    "crush": "Payal",
    "fav. subject": "Maths",
    "dream": "Youtuber and multimillionare"
    }
Aman["health"] = "Bad"
print(Aman["health"])

Aman["emotional control"] = "Insane"
print(Aman["emotional control"])

print("crush" in Aman)
print("gf" not in Aman)
print(Aman.keys())

for key in Aman.keys():
    print("Kabhi kisi se pyaar mat karna because of",key)
    
print(Aman.values())

for value in Aman.values():
    print("Kabhi kisi ko dhokha mat dena because of",value)

for key,value in Aman.items():
        print(key,":",value)
        
print("i wanna marry",Aman.get("crush","No"))  

   
Aman.update({
    "health": "Good",
    "emotional control": "tragedy"
  
})         

print(Aman["emotional control"])
  
        
Downfall = Aman.pop("fav. subject") 
del Aman["health"]

x = input("wanna delete dictionary: ")
if x == "yes":
    Aman.clear()
    print("Life destroyed")
else:
       print("Live ur life")
if len(Aman) >= 0:
       for key,value in Aman.items():
           print(key,":",value)      
       
       
        