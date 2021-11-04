city_names=["Oakland", "Atlanta", "New York City", "Seatle", "Memphis", "Miami", "Boston", "Los Angeles", "Denver", "New Orleans"]
print(city_names)

dog_breeds=["Bulldog", "Labrador Retriever", "Poodle", "German Shepherd", "Golden Retriever", "Siberian Husky", "Dachshund", "Chihuahua", "Pomeranian", "Yorkshire Terrier"]
print(dog_breeds)

city_names[7]
city_names[5]
city_names[0]

dog_breeds[3]
dog_breeds[4]
dog_breeds[1]

favorite_city=city_names[0:3]
favorite_dog_breeds=dog_breeds[0:4]

city_names[0]="San  Francisco"
city_names[2]="Brookyln"
city_names[7]="Hollywood"
city_names[5]="Tampa"

city_names.append("Oakland")
city_names.extend(["New York City", "Los Angeles"])
city_names.insert(0, "Miami")
print(city_names)

del city_names[3]
city_names.pop(5)
city_names.remove("Miami")
print(city_names)

def city_names():
    print(city_names)
