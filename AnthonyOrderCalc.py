# how many items were ordered
green_teas = 2
sushi_plates = 6

# the prices of each item
green_tea_price = 2.50
sushi_plate_price = 1.50

# the totals for each item
print(green_teas * green_tea_price)
print(sushi_plates * sushi_plate_price)

# the grand total of all items combined
total = green_teas * green_tea_price + sushi_plates * sushi_plate_price
print("total:", total)

# ask the user what percent tip they will add,
# save that number into a variable
tip_percent = int(input("What percent tip will you add?"))

# tell the user the final tip amount
print("The tip amount comes to " + str(total * tip_percent / 100))
