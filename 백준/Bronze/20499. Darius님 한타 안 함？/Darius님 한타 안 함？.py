KDA = input().split("/")

kill = int(KDA[0])
death = int(KDA[1])
assist = int(KDA[2])

if kill + assist < death or death == 0:
    print("hasu")
else:
    print("gosu")