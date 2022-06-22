text = input()
store = dict()

while text != "statistics":
    text = text.split(":")
    product = text[0]
    quantity = int(text[1])

    if product in store.keys():
        store[product] += quantity
    else:
        store[product] = quantity

    text = input()

count = len(store.keys())
total = sum(store.values())

print(f"Products in stock:")

for product in store:
    print(f"- {product}: {store[product]}")
print(f"Total Products: {count}")
print(f"Total Quantity: {total}")
