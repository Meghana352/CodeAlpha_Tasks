stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 300
}

total = 0

print("Stock Portfolio Tracker")

while True:
    name = input("Enter stock name or 'done': ").upper()

    if name == "DONE":
        break

    if name in stock_prices:
        qty = int(input("Enter quantity: "))
        value = stock_prices[name] * qty
        total += value
        print("Added value:", value)
    else:
        print("Stock not found")

print("Total investment:", total)