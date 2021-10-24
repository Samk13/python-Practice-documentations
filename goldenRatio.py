from functools import lru_cache


@lru_cache(maxsize=1000)
def fibonacci(n):
    """return the fibonacci number of n"""
    # check if the input is int
    if type(n) != int:
        raise TypeError("n must be a positive int")
    # check if the input is positive
    if n < 1:
        raise ValueError("n must be a positive int")
    # check if the input is greater than 1
    if n == 1:
        return 1
    if n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


for n in range(1, 100):
    print(n, ":", fibonacci(n + 1) / fibonacci(n))
