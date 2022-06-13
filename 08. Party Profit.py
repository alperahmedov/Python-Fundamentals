group = int(input())
days = int(input())
coins = 0

for day in range(1, days + 1):
    coins += 50

    if day % 10 == 0:
        group -= 2

    if day % 15 == 0:
        group += 5

    coins -= int(group * 2)

    if day % 3 == 0:
        coins -= int(group * 3)

    if day % 5 == 0:
        coins += int(20 * group)

    if day % 5 == 0 and day % 3 == 0:
        coins -= int(group * 2)

coins = int(coins)
result = int(int(coins) / group)

print(f"{group} companions received {result} coins each.")
