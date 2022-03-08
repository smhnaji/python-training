def distance_method_1(a, b):
    x1, y1 = a
    x2, y2 = b
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

# ORRRRRRRR

def distance_method_2(a, b):
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5


print(
    distance_method_1((1, 2), (10, 20)),
    distance_method_2((1, 2), (10, 20)),
)