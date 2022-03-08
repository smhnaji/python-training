number = int(input())
power = 1

while(2 ** power < number):
    power += 1

print(2 ** power)