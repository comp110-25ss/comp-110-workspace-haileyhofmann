def value_check(a: int, b: int, c: float) -> float:
    b = b + 1
    if a % b == 0:
        c = a / b
    else:
        c = float(a % b)
    c = c + 2.0
    return c


print(value_check(a=4, b=1, c=0.0))
