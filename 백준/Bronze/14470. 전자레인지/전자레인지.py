meat_degree = int(input())
target_degree = int(input())
froze_meat_heating_per_time = int(input())
melting_frozen_meat = int(input())
unfrozen_meat_heating_per_time = int(input())

answer = 0
isFrozen = 0

while meat_degree != target_degree:
    if meat_degree < 0:
        answer += froze_meat_heating_per_time * (0 - meat_degree)
        meat_degree = 0
        isFrozen = 1
    else:
        if isFrozen == 1:
            answer += melting_frozen_meat
            isFrozen = 0
        else:
            answer += unfrozen_meat_heating_per_time * (target_degree - meat_degree)
            meat_degree = target_degree

print(answer)