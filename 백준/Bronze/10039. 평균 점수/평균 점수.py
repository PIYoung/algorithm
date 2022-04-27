s1 = int(input())
s2 = int(input())
s3 = int(input())
s4 = int(input())
s5 = int(input())

s1 = s1 if s1 >= 40 else 40
s2 = s2 if s2 >= 40 else 40
s3 = s3 if s3 >= 40 else 40
s4 = s4 if s4 >= 40 else 40
s5 = s5 if s5 >= 40 else 40

print(f'{(s1 + s2 + s3 + s4 + s5) // 5}')