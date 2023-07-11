import random
from typing import Any
l: list[list[int]] = []
for _ in range(4):
    l1 = []
    for i in range(4):
        l1.append(random.randint(1, 9))
    l.append(l1)
a = l[0]
b = l[1]
c = l[2]
d = l[3]
print(f"{a}\n{b}\n{c}|n{d}")
l2: list[Any] = []
l2 = a + b + c + d
print(l2)
si = 0
for i in range(1,10):
    if l2.count(i) == 1:
        si = si + 1
print(si)
print((si/16)*100)