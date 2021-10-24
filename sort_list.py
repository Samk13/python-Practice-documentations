data = [
    {'name': 'John', 'age': 20},
    {'name': 'Bob', 'age': 30},
    {'name': 'Alice', 'age': 25},
    {'name': 'Kate', 'age': 22},
    {'name': 'Jack', 'age': 18},
]

sort_data = sorted(data, key=lambda x: x['age'], reverse=True)
print(sort_data)
