# Stock Portfolio Tracker

# Hardcoded stock prices (dictionary)
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 2700,
    "MSFT": 320
}

total_investment = 0
portfolio = {}

# Taking user input
n = int(input("Enter number of stocks you want to buy: "))

for i in range(n):
    stock_name = input("Enter stock name (AAPL, TSLA, GOOG, MSFT): ").upper()
    quantity = int(input("Enter quantity: "))
    
    if stock_name in stock_prices:
        investment = stock_prices[stock_name] * quantity
        total_investment += investment
        portfolio[stock_name] = quantity
    else:
        print("Stock not available!")

# Display result
print("\nYour Portfolio:")
for stock, qty in portfolio.items():
    print(f"{stock} : {qty} shares")

print(f"\nTotal Investment Value = ${total_investment}")

# Save to file (optional)
save = input("\nDo you want to save the result to a file? (yes/no): ").lower()

if save == "yes":
    with open("portfolio.txt", "w") as file:
        file.write("Stock Portfolio\n")
        for stock, qty in portfolio.items():
            file.write(f"{stock} : {qty} shares\n")
        file.write(f"\nTotal Investment Value = ${total_investment}")
    print("Data saved to portfolio.txt")