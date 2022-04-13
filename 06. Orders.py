num_of_orders = int(input())
total = 0

for o in range(num_of_orders):
    price = float(input())
    days = int(input())
    capsules = int(input())
    order_price = price * days * capsules
    total += order_price
    print(f"The price for the coffee is: ${order_price:.2f}")

print(f"Total: ${total:.2f}")