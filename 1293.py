from functools import reduce
print(2 * reduce(lambda x, y: x*y, map(int, input().split())))
