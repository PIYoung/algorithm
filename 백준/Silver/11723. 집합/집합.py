from sys import stdin

M = int(stdin.readline())
my_set = set()
all = set([_ for _ in range(1, 21)])

for _ in range(M):
    my_list = stdin.readline().split()

    if len(my_list) == 1:
        if my_list[0] == "all":
            my_set = all
        else:
            my_set = set()
    else:
        command, value = my_list
        value = int(value)

        if command == "add":
            my_set.add(value)
        elif command == "remove":
            my_set.discard(value)
        elif command == "check":
            print(1 if value in my_set else 0)
        elif command == "toggle":
            if value in my_set:
                my_set.discard(value)
            else:
                my_set.add(value)