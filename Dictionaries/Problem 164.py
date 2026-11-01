# Filter a Dict by Condition

prices = {"pen": 10, "book": 150, "bag": 500, "pencil": 5}

cheap = {name: price for name, price in prices.items() if price < 100}

print(cheap)