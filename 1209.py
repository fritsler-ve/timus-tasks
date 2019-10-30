# 1209
from math import sqrt


def value(number):
    return int((1 + sqrt(1 + 8 * number)) / 2) - 1


def nvalue(number):
    return int(((number + 1) * number) / 2)


def solve(number):
    n = value(number)
    if (nvalue(value(number)) == number - 1):
        return 1
    if (nvalue(value(number) + 1) == number - 1):
        return 1
    if (nvalue(value(number) - 1) == number - 1):
        return 1
    return 0

N = int(input())
for i in range(N):
    print(solve(int(input())), end=' ')
