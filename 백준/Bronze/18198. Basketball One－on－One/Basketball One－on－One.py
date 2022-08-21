record = input()
A = 0
B = 0

for i in range(len(record)):
    if record[i] == 'A':
        A += int(record[i + 1])
    elif record[i] == 'B':
        B += int(record[i + 1])
        
print('A' if A > B else 'B')