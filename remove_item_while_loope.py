a = [1, 2, 34, 4, 4, 5, 6, 7, 8, 9, 10]

print("------------------------------------------------------")
print(a[::2])
print("------------------------------------------------------")


def even(x):
    return x % 2 == 0


# [::2] is the same as [start:stop:step]
# [:] is the same as [start:stop] and malke a copy of the list
for item in a[:]:
    if even(item):
        a.remove(item)

print(a)
