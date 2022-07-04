m, s, g = map(float, input().split())
a, b = map(float, input().split())
l, r = map(float, input().split())

ls = m / g + 1 if m % g else m / g
rs = m / s + 1 if m % s else m / s
lw = l / a
rw = r / b

if ls < rs:
    if ls + lw < rs + rw:
        print("friskus")
    else:
        print("latmask")
else:
    if ls + lw < rs + rw:
        print("friskus")
    else:
        print("latmask")