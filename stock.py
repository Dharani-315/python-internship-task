stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 2700,
    "MSFT": 300,
    "AMZN": 3300
}

portfolio = {}

n = int(input("How many stocks do you want to add? "))

for i in range(n):
    stock = input("Enter stock name: ").upper()
    quantity = int(input("Enter quantity: "))
    
    portfolio[stock] = quantity

total_value = 0

for stock, quantity in portfolio.items():
    if stock in stock_prices:
        price = stock_prices[stock]
        total_value += price * quantity
    else:
        print(stock, "not found in price list")

print("Total Investment Value:", total_value)

# Save to file
with open("portfolio.txt", "w") as file:
    file.write("Stock Portfolio\n")
    
    for stock, quantity in portfolio.items():
        file.write(f"{stock} - {quantity}\n")
    
    file.write(f"\nTotal Value: {total_value}")
