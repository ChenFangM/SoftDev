"""
JFCCC: Fang Chen, Jeff Chen
Soft Dev, pd 2

DISCO:
Access dict items w/ dictName[key] or dictName.get(key())

QCC:
Why does...

    from random import seed
    from random import randint
    for _ in range(2):
        print(randint(0, 2))

... only print 2 [newline] 0?

OPS Summary:

"""
import random

krewes = {2:["Jeff", "Fang"], 7:["7Devo1", "7Devo2"], 8:["8Devo1", "8Devo2"]}
print((krewes[2])[random.randint(0,2)])

for _ in range(2):
    print(random.randint(0, 2))