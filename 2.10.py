a = int(input())
b = int(input())
c = int(input())

if (a*a == b*b + c*c) or (b*b == a*a + c*c) or (c*c == a*a + b*b):
    print('YES')
else:
    print('NO')