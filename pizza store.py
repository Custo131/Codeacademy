# Your code below:
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

#prices
prices = [4, 3, 6, 8, 2, 9, 2]

num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices) 

# finding the length of the toppings list
num_pizzas = len(toppings)
# Our daily phrase

print("We sell" + " " + str(num_pizzas) + " " + "different kinds of pizza!")
#price list 
pizza_and_prices = [[4, "pepperoni"], [3, "pineapple"], [6, "cheese"], [8, "sausage"], [2, "olives"], [9, "anchovies"], [1, "mushrooms"],   [2.5, "peppers"]]
#sorting prices 
pizza_and_prices.sort()
print(pizza_and_prices)

#cheapest pizza
cheapest_pizza = pizza_and_prices[0]
print("Our cheapest pizza:", cheapest_pizza)

#most expensive pizza
priciest_pizza = pizza_and_prices[6]
print("Our most EXPENSIVE PIZZA:", priciest_pizza)
#bought pizza
pizza_and_prices.pop(6)

#three cheapest pizza 
three_cheapest_list = [[1, 'mushrooms'], [2, 'olives'], [2.5, 'peppers']]
print("Our three cheapest pizza:", three_cheapest_list)






