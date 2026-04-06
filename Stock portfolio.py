stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 2800,
    "AMZN": 3300,
    "MSFT": 300
}

portfolio = {}
total_investment = 0

print("📈 Stock Portfolio Tracker")
print("Available stocks:", ", ".join(stock_prices.keys()))
while True:
    stock = input("\nEnter stock name (or 'done' to finish): ").upper()
    
    if stock == "DONE":
        break
    
    if stock not in stock_prices:
        print("❌ Stock not available!")
        continue
    
    quantity = int(input(f"Enter quantity of {stock}: "))
    
    portfolio[stock] = quantity
print("\n📊 Your Portfolio:")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    investment = price * qty
    total_investment += investment
    print(f"{stock}: {qty} shares × ${price} = ${investment}")

print("\n💰 Total Investment Value: $", total_investment)
save = input("\nDo you want to save to file? (yes/no): ").lower()

if save == "yes":
    with open("portfolio.txt", "w") as file:
        file.write("Stock Portfolio Summary\n")
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            investment = price * qty
            file.write(f"{stock}: {qty} × ${price} = ${investment}\n")
        file.write(f"\nTotal Investment: ${total_investment}")
    
    print("✅ Portfolio saved to portfolio.txt")