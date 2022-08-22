while True:
    name, age, weight = input().split()
    age, weight = int(age), int(weight)
    
    if name == '#' and age == 0 and weight == 0:
        break

    if age > 17 or weight >= 80:
        print("%s Senior" % name)
    else:
        print("%s Junior" % name)