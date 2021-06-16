def fct1(x):
    if x < 0:
        return 0
    return x + fct1(x-1)


def fct2(x):
    if x % 2:
        x -= 1
    if x < 0:
        return 0
    return x + fct2(x-2)


def fct3(x):
    if not x % 2:
        x -= 1
    if x < 0:
        return 0
    return x + fct3(x-2)


print(fct1(10))

print(fct2(10))

print(fct3(10))
