n = int(input())

i = 0
j = 0
columns = 0
line = ''

while (i < n):
    while (columns < n):
        j += i
        columns += 1
        line += str(columns + j) + ' '
    i += 1
    j = 0
    columns = 0
    print(line)
    line = ''