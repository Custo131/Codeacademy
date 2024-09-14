hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]
#task 1

total_price = 0
#task 2

for price in prices:
  total_price += price
print(total_price)

#task 3 

average_price = total_price/len(prices)

#task 4

print("Average Haircut Price:",average_price)
#task 5

new_prices = [new_prices - 5 for new_prices in prices]
#task 6
print("New prices:", new_prices)
#task 7 
total_revenue = 0
#task 8
for i in range(len(hairstyles)):
    total_revenue += prices[i] * last_week[i]
print("Total Revenue:", total_revenue)
average_daily_revenue = total_revenue/7
print("Average Daily Revenue:", average_daily_revenue)

cuts_under_30 = [hairstyles[i] for i in range(len(new_prices) - 1) if new_prices[i] < 30]
print("Haircuts under 30:", cuts_under_30)

  






