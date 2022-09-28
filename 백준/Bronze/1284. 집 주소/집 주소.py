while True:
    N = input()
    if N == '0':
        break
        
    answer = len(N) + 1
    for n in N:
        if n == '0':
            answer += 4 
        elif n == '1':
            answer += 2
        else:
            answer += 3
            
    print(answer)