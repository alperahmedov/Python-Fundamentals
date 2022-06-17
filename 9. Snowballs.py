best_snowball_quality = 0
best_snow_data = ""
number_of_snowball = int(input())

for _ in range(number_of_snowball):
    weight = int(input())
    time = int(input())
    quality = int(input())

    result = (weight / time) ** quality

    if result > best_snowball_quality:
        best_snowball_quality = result
        best_snow_data = (f'{weight} : {time} = {int(result)} ({quality})')
print(best_snow_data)
