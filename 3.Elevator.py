number_of_person = int(input())
capacity = int(input())
result = 0

if capacity > number_of_person:
    result += 1
else:
    result = number_of_person // capacity
    if number_of_person % capacity != 0:
        result += 1

print(result)