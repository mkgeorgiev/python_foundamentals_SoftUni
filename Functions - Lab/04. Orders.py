product = input()
quantity = int(input())
order = lambda product_price: product_price * quantity

coffee_price = 1.5
water_price = 1
coke_price = 1.4
snacks_price = 2

if product == "coffee":
    product_price = coffee_price
elif product == "water":
    product_price = water_price
elif product == "coke":
    product_price = coke_price
elif product == "snacks":
    product_price = snacks_price
print(f"{order(product_price):.2f}")