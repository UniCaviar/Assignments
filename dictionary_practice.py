from types import GeneratorType


grocery_items={"Chicken":"$1.59", "Beef":"$1.99", "Cheese":"$1.00", "Milk":"$2.50"}

print(grocery_items["Chicken"])
print(grocery_items["Beef"])
print(grocery_items["Cheese"])
print(grocery_items["Milk"])

video_games={"Persona 5 Royal":"$59.99", "Persona 4 Golden":"$19.99", "Legend of Zelda Breath of the Wild":"$59.99", "Grand Theft Auto 5":"$29.99"}

print(video_games["Persona 5 Royal"])
print(video_games["Persona 4 Golden"])
print(video_games["Legend of Zelda Breath of the Wild"])
print(video_games["Grand Theft Auto 5"])

shoe_names={"Jordan 13": 1, "Yeezy": 8, "Foamposite": 10, "Air Max": 5, "SB Dunk": 20}
shoe_names.update({"SB Dunk":22})
print(shoe_names["SB Dunk"])
shoe_names.update({"Yeezy":7})
print(shoe_names["Yeezy"])

shoe_names.update({"Jordan 13":8})
shoe_names.update({"Yeezy":14})
shoe_names.update({"Foamposite":17})
shoe_names.update({"Air Max":12})
shoe_names.update({"SB Dunk":29})
print(shoe_names)

shoe_names.update({"Jordan 13":3})
shoe_names.update({"Yeezy":11})
shoe_names.update({"Foamposite":14})
shoe_names.update({"Air Max":9})
shoe_names.update({"SB Dunk":26})
print(shoe_names)

grocery_items["Bread"]="$3.99"
grocery_items["Cereal"]="$4.99"
grocery_items["Banana"]="$1.50"

video_games["Persona 3 FES"]= "$29.99"
video_games["Grand Theft Auto The Trilogy"]="59.99"
video_games["Pokemon Brilliant Diamond"]="$59.99"

shoe_names["Low 1"]=10
shoe_names["Capri Onyx"]=5
shoe_names["Air Force 1"]=15

del grocery_items["Chicken"]
del grocery_items["Cheese"]
print(grocery_items)

del video_games["Pokemon Brilliant Diamond"]
del video_games["Persona 3 FES"]
print(video_games)

del shoe_names["Air Max"]
del shoe_names["Jordan 13"]
print(shoe_names)

