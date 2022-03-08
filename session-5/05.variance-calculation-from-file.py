from pathlib import Path

print(__file__)


with open('scores.txt', 'r'):
    for line in file.readlines():
        scores.append([int(x) for x in line.strip().split(',')])
print(scores)


variances = []
for i in range(len(scores[0])):
    c = [x[i] for x in scores]
    m = sum(c) / len(c)
    variance = sum([(x - m) ** 2 for x in c]) / len(c)
    variances.append(v)


print(variances)