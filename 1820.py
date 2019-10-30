# 1820

from math import ceil

n, k = map(int, input().split())
if (n <= k):
    print(2)
else:
    print(int(ceil(n * 2 / k)))
