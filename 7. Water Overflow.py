tank_capacity = 255
numbers_of_line = int(input())
capacity = 0

for n in range(numbers_of_line):
    liters_of_water = int(input())
    capacity += liters_of_water
    if capacity > tank_capacity:
        capacity -= liters_of_water
        print("Insufficient capacity!")
        continue
print(capacity)
