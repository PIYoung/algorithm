while True:
    sentence = input()
    
    if sentence == "END":
        break
        
    answer = sentence[::-1]
    
    print(answer)