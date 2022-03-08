r, c = input().split()
r = int(r)
c = int(c)

r = abs(11 - r)

y = 0
x = r

direction = 'Right'
if c > 10:
    direction = 'Left'
    # c -= 11
    x = 10 - r
else:
    y = c #abs(c - 10) + 1

print(direction, y, x)