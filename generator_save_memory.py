import sys

# using lists
my_list = [i for i in range(1, 1000001)]
print(sum(my_list))
print(sys.getsizeof(my_list), "bytes")

# using generators (less memory)
my_generator = (i for i in range(1, 1000001))
print(sum(my_generator))
print(sys.getsizeof(my_generator), "bytes")
