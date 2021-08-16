item_count = int(input("How many items would you like to add up"))
count = 0
total_price = 0
if item_count == 0:
    print("invalid Option")
    item_count = int(input("How many items would you like to add up"))
while count != item_count :
    count = count + 1
    price = float(input("How much is the item"))
    total_price = price + total_price
    pass
else:
    print("Number of items counted = ",item_count)
    total_cost = print("Here is your final total $",total_price)

