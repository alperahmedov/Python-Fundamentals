lost_fight_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
expenses = 0
count = 0

for _ in range(1, lost_fight_count + 1):
    if _ % 2 == 0:
        expenses += helmet_price
    if _ % 3 == 0:
        expenses += sword_price
    if _ % 6 == 0:
        expenses += shield_price
        count += 1
    if count != 0 and count % 2 == 0:
        expenses += armor_price
        count = 0

print(f"Gladiator expenses: {expenses:.2f} aureus")
