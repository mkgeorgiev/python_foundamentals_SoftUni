shop = input().split("|")
budget = float(input())
selling_price = 0
total_profit = 0
starting_budget = budget
valid_shopping_item_list = [["Clothes", 50.00], ["Shoes", 35.00], ["Accessories", 20.50]]

for shop_item in range(len(shop)):
    shop_items = shop[shop_item].split("->")
    price = float(shop_items[1])
    for item_type in range (len(valid_shopping_item_list)):
        if shop_items[0] == valid_shopping_item_list[item_type][0]:
            if price <= valid_shopping_item_list[item_type][1]:
                if budget >= price:
                    budget -= price
                    selling_profit = 0.4 * price
                    total_profit += selling_profit
                    print(f"{selling_profit+price:.2f}", end=" ")
print()
print(f"Profit: {total_profit:.2f}")
if total_profit + starting_budget >= 150:
    print("Hello, France!")
else:
    print("Time to go.")



