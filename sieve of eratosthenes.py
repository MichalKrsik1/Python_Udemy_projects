def soe_prime(n):
    numbers = list(range(2, n + 1))

    for number in numbers:
        if number:
            for i in range(number * 2, n + 1, number):
                numbers[i - 2] = 0

    return [num for num in numbers if num]
