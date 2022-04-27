import sys

f_burger = int(sys.stdin.readline())
s_burger = int(sys.stdin.readline())
t_burger = int(sys.stdin.readline())
cola = int(sys.stdin.readline())
cider = int(sys.stdin.readline())

cheap_burger = min(f_burger, s_burger, t_burger)
cheap_beverage = min(cola, cider)

print(cheap_burger + cheap_beverage - 50)