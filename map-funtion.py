temp = [
    ("Berlin", 29),
    ("Cairo", 36),
    ("Buenos Aires", 19),
    ("Los Angeles", 26),
    ("Tokyo", 27),
    ("New York", 28),
    ("London", 22),
    ("Beijing", 32),
    ("Moscow", 20),
]


def c_to_f(data):
    return data[0].capitalize(), (9 / 5) * data[1] + 32


print(list(map(c_to_f, temp)))
