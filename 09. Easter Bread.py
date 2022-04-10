budget = float(input())
flour_price = float(input())
bread_count = 0
colored_eggs = 0
spend_money = 0

egg_price = flour_price * 0.75
milk_price = (flour_price + (flour_price * 0.25)) / 4

one_bread_price = flour_price + egg_price + milk_price

while budget - spend_money > 0:

    if budget < spend_money + one_bread_price:
        break

    else:
        bread_count += 1
        colored_eggs += 3
        spend_money += one_bread_price

    if bread_count % 3 == 0:
        colored_eggs -= (bread_count - 2)

money_left = budget - spend_money
print(f"You made {bread_count} loaves of Easter bread! Now you have {colored_eggs} eggs and {money_left:.2f}BGN left.")
