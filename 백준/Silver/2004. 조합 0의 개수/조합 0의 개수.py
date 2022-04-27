n, m = map(int, input().split())


def count_two(n):
    result = 0

    while n != 0:
        n //= 2
        result += n

    return result


def count_five(n):
    result = 0

    while n != 0:
        n //= 5
        result += n

    return result


five_count = count_five(n) - count_five(n - m) - count_five(m)
two_count = count_two(n) - count_two(n - m) - count_two(m)

print(min(two_count, five_count))