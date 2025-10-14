import matplotlib.pyplot as plt
plt.style.use('ggplot')
x = [1, 2, 3, 4, 5]
sales = [10, 20, 30, 25, 35]
profit = [2, 5, 8, 6, 10]
plt.plot(x, sales, label='Sales', marker='o')
plt.plot(x, profit, label='Profit', marker='s')
plt.title("Sales vs Profit Trend")
plt.xlabel("Quarter")
plt.ylabel("Amount ($)")
plt.legend()
plt.savefig("sales_profit_chart.png")   # save the plot
plt.show()
 