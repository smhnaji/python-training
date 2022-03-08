# mode can be [w]rite, [r]ead, [a]ppend

f = open('data-structure/data.txt', 'r')

lineCounter = 0
total0 = 0
total1 = 0
total2 = 0
total3 = 0

for line in f.readlines():
    lineCounter += 1
    scores = line.split(',')
    total0 += float(scores[0])
    total1 += float(scores[1])
    total2 += float(scores[2])
    total3 += float(scores[3])

print(f'{total0 / lineCounter}, {total1 / lineCounter}, {total2 / lineCounter}, {total3 / lineCounter}')