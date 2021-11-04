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

def print_city(list):
    list= city_names
    return list

def reorangize_list(list):
    # [1,2,3,4,5]
    print(list)
    counter=0

    while counter < len(list):
        item1 = list[counter]
        item2 = list[counter +1]

        if len(item1) >= len(item2):
            counter += 1
            continue
        elif counter + 1 == len(list) - 1:
            break
        else:
            list.remove(item1)
            list.append(item1)
            counter += 1

            return list

def print_favorite_dogs(list):
    list=favorite_dog_breeds
    return list
