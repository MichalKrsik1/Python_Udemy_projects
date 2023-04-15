def loop_factorial(n):
    result = 1

    while n > 0:
        result *= n
        n -= 1

    return result


def recursive_factorial(n):
    if n == 1:
        return 1
    return n * recursive_factorial(n - 1)
