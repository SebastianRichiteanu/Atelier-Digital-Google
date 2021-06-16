def sum_function(*args, **kargs):
    sum = 0
    for x in args:
        if isinstance(x, int) or isinstance(x, float):
            sum += x
    return sum


print(sum_function(1, 5, -3, 'abc', [12, 56, 'cad']))
print(sum_function())
print(sum_function(2, 4, 'abc', param_1=2))


def is_integer():
    x = input()
    try:
        x = int(x)
    except ValueError:
        return 0
    else:
        return x


print(is_integer())

