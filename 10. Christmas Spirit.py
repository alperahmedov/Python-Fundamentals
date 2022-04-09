quantity = int(input())
days = int(input())
christmas_spirit = 0
total_cost = 0
ornament_set = 2
tree_skirt = 5
tree_garlands = 3
tree_lights = 15


for day in range(1, days + 1):
    condition_5th_day = False
    if day % 11 == 0:
        quantity += 2

    if day % 2 == 0:
        total_cost += ornament_set * quantity
        christmas_spirit += 5

    if day % 3 == 0:
        total_cost += (tree_skirt * quantity) + (tree_garlands * quantity)
        christmas_spirit += 13
        condition_5th_day = True

    if day % 5 == 0:
        total_cost += tree_lights * quantity
        christmas_spirit += 17

        if condition_5th_day:
            christmas_spirit += 30

    if day % 10 == 0:
        christmas_spirit -= 20
        total_cost += 23

        if day == days:
            christmas_spirit -= 30


print(f"Total cost: {total_cost}")
print(f"Total spirit: {christmas_spirit}")

