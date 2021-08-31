import random


def my_random ():
    # random between 3 and 7
    return 3 * random.random() + 7

# for i in range(10):
#     print(random.randint(3, 7), end=' ')

# play rock paper scissors
outcomes = ['rock', 'paper', 'scissors']
for i in range(20):
    print(random.choice(outcomes))

print(random.socratica()) # random.socratica() is a random number between 0 and 1
