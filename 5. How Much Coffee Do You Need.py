command = input()

event_list_lower = ["coding", "dog", "cat", "movie"]
event_list_upper = ["CODING", "DOG", "CAT", "MOVIE"]

coffee_counter = 0

while command != "END":

    if command in event_list_upper:
        coffee_counter += 2
    elif command in event_list_lower:
        coffee_counter += 1

    command = input()

    if command == "END":
        if coffee_counter > 5:
            print(f'You need extra sleep')
        else:
            print(coffee_counter)
