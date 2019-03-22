def sqrt(x):
    y = x
    while abs(y*y - x) >= 1e-10:
        y = (y + x/y) / 2
    return y

print(sqrt(10))