# a, b = 0,1
# while b < 49:
#     print(b, end=' ')
#     a, b = b, a+b

# def fib(n):
#     """Print a Fibonacci series up to n."""
#     a, b = 0, 1
#     while b < n:
#         print(b, end=' ')
#         a, b = b, a+b
#     print()


def func(a=1, b=2, *args):
    print(a, b)
    # print(args)
    for i in args:
        print(i, end=" ")
    # print(kwargs)


inp = {"a": 1000, "b": 300}
func(**inp)
pairs = [(1, "one"), (2, "two"), (3, "three"), (4, "four")]
pairs.sort(key=lambda pair: pair[1])
