a = []
for i in range(1, 101, 2):
    if i % 5 == 0:
        a.append(i * 100)

print(a)

################################

print([i * 100 for i in range(1, 101, 2) if i % 5 == 0])

# generates a LIST
print([i * 100 if i > 50 else 99999 for i in range(1, 101, 2) if i % 5 == 0])

# generates a GENERATOR
a = ((i * 100 if i > 50 else 99999 for i in range(1, 101, 2) if i % 5 == 0))
print(type(a))
print(a)