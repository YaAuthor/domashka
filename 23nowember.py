from itertools import *
def F(x,y,z,w):
    return (not((not(y) <=x)<=w)) or(z<=x)
for x1, x2, x3, x4, x5, x6 in product(range(2), repeat=6):
    t = [(x1, 0, 0, x2), (x3, 1, 1, 0), (x4, 1, x5, x6)]
    if len(t) == len(set(t)):
        for i in permutations('xyzw'):
            if [F(**dict(zip(i, r))) for r in t] == [0, 0, 0]:
                print(i)