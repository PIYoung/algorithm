while True:
    branchorama = list(map(int, input().split()))
    
    if branchorama[0] == 0:
        break
        
    n = 1
    for branch in range(branchorama[0]):
        sf = branchorama[2 * branch + 1]
        p = branchorama[2 * branch + 2]
        n = n * sf - p
        
    print(n)