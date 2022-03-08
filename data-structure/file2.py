f = open('data-structure/data.txt', 'r')

lineCounter = 0

totals = [0, 0, 0, 0]

for line in f.readlines():
    lineCounter += 1
    scores = line.split(',')

    for i in totals:
        print(i)
        totals[i] += float(scores[i])

print (totals)

# Find the 4 variances

# avg0 = total0 / lineCounter
# avg1 = total1 / lineCounter
# avg2 = total2 / lineCounter
# avg3 = total3 / lineCounter

# for line in f.readlines():
