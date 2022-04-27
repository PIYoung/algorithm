x_per_price = int(input())
y_base_price = int(input())
y_limit = int(input())
y_per_price = int(input())
p_usage = int(input())

x_price = x_per_price * p_usage
y_price = y_base_price

if p_usage > y_limit:
    y_price = y_base_price + (p_usage - y_limit) * y_per_price

print(min(x_price, y_price))