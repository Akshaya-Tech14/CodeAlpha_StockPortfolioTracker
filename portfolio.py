stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 150,
    "MSFT": 300
}

total_value = 0

print("===== STOCK PORTFOLIO TRACKER =====")

while True:

    stock = input("Enter Stock Name (or DONE): ").upper()

    if stock == "DONE":
        break

    if stock in stocks:

        quantity = int(input("Enter Quantity: "))

        value = stocks[stock] * quantity
        total_value += value

        print("Value:", value)

    else:
        print("Stock Not Available")

print("\nTotal Investment Value = $", total_value)

file = open("portfolio.txt", "w")
file.write("Total Investment Value = $" + str(total_value))
file.close()

print("Data saved in portfolio.txt")
