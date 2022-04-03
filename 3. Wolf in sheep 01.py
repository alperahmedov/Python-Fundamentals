animal = input().split(", ")
list_of_animals = animal

list_of_animals.reverse()
counter = 0
n = len(list_of_animals)

for i in range(n):
    if list_of_animals[i] == "wolf" and i == 0:
        print("Please go away and stop eating my sheep")
        break
    elif list_of_animals[i] == "wolf" and i != 0:
        counter += i
        print(f"Oi! Sheep number {counter}! You are about to be eaten by a wolf!")
        break
