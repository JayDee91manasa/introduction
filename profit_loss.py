actual_profit = float(input(" Please Enter the Actual Product Price: "))
sale_amount = float(input(" Please Enter the Sales Amount: "))

if (sale_amount > actual_profit):
    amount = sale_amount - actual_profit
    print("Total Profit = {0}".format(amount))
else:
    print("No Profit!!!")
