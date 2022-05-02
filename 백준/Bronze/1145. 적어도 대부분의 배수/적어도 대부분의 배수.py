import gc
from math import gcd

data_list = list(map(int, input().split()))

candidate_list = []

for i in range(5):
    for j in range(i + 1, 5):
        for k in range(j + 1, 5):
            lcm = data_list[i] * data_list[j] // gcd(data_list[i], data_list[j])
            lcm = lcm * data_list[k] // gcd(lcm, data_list[k])
            candidate_list.append(lcm)

print(min(candidate_list))