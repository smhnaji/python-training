for i in range(0, 10, 2):
    print(i)

for key, value in enumerate([10, 20, 30]):
    print(key, value)

for a, b in zip([10, 20, 30], [100, 200, 300, 2222]):
    print(a, b)
    # note that 2222 is skipped

for a, b in zip([10, 20, 30, 40, 50000], [100, 200, 300, 2222]):
    print(a, b)
    # note that 50000 is skipped

for a, b, c, d, e in zip([1], [10], [100], [1000], [10000]):
    print(a, b, c, d, e)

for key, value in enumerate(zip([1], [10], [100], [1000], [10000])):
    a, b, c, d, e = value
    print(key, value)
    print(a, b, c, d, e)
