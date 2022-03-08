# Khar dar chaman

a, b, l = input().split()
a = int(a)
b = int(b)
l = int(l)

totalSeconds = 0
lastWaiting = 'b'
currentCount = 0

while currentCount < l:
    currentCount += 1
    if lastWaiting == 'b':
        totalSeconds += a
        lastWaiting = 'a'
    else: # if lastWaiting == 'a':
        totalSeconds += b
        lastWaiting = 'b'

print(totalSeconds)
