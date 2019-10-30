# TL 8

first = [input() for i in range(int(input()))]
second = [input() for i in range(int(input()))]
res = 0
f = set(first)
for i in second:
    if i in f:
        res += 1
print(res)
