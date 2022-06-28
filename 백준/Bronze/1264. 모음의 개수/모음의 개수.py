while 1:
    s = input()
    if s == '#':
        break
    cnt = 0
    for c in s:
        if c in 'aeiouAEIOU':
            cnt += 1
    print(cnt)