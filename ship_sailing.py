weight = 4.5


#Ground shipping 
if weight <= 2:
  print(1.50 * weight + 20.00)
elif weight > 2  and weight <= 6:
  print(weight * 3.00 + 20.00)
elif weight > 6 and weight <= 10:
  print(weight *4.00 + 20.00)
elif weight > 10:
  print(weight * 4.75 + 20.00)
  print("Ground shipping:"+ weight)

premium_ground_shipping = 125.00
print("premium ground shipping =", premium_ground_shipping)

#Drone Shipping 
if weight <= 2:
  print(weight * 4.50)
elif weight > 2 and weight <= 6:
  print(weight * 9.00)
elif weight > 6 and weight <= 10:
  print(weight * 12.00)
elif weight > 10:
  print(weight* 14.25)
  print("Drone shipping:", weight)

print("The most cheapest method of shipping", weight, "lb", 
          "is Ground shipping\n")