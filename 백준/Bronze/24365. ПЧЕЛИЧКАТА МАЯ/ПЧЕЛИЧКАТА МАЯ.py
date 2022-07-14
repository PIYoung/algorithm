A, B, C = map(int, input().split())

v = [{"second": 0}, {"second": 1}, {"second": 2}]
v[0]["first"] = A
v[1]["first"] = B
v[2]["first"] = C

avg = (v[0]["first"] + v[1]["first"] + v[2]["first"]) / 3
ans = abs(v[2]["second"] - v[0]["second"]) * (avg - v[0]["first"]) + abs(
    v[2]["second"] - v[1]["second"]
) * (avg - v[1]["first"])

print(int(ans))