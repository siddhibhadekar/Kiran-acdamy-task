cost_price = 1200
selling_price = 1500

if selling_price > cost_price:
    profit = selling_price - cost_price
    print("Profit is", profit)
elif cost_price > selling_price:
    loss = cost_price - selling_price
    print("Loss is", loss)
else:
    print("No profit, no loss")
