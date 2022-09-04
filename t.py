import random
key = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
a = '@'
for n in range(1):
    b=''
    for i in range(5):
        b += (random.choice(key))
        c=a+b
        print(c)