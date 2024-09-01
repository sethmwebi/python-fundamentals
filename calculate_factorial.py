def calculate_factorial(n: int) -> int:
    if n < 1:
        return 1
    else:
        n = n * calculate_factorial(n - 1)
    return n


print(calculate_factorial(120))
