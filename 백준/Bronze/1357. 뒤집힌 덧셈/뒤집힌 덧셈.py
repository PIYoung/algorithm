X, Y = input().split()


def Rev(n):
    result = ""

    for i in reversed(n):
        result += i

    return result


print(int(Rev(str(int(Rev(X)) + int(Rev(Y))))))