# 1787

k, n = map(int, input().split())
a = list(map(int, input().split()))

i = 0
temp = 0
while (n > 0):
    temp = max(a[i] + temp - k, 0)
    n -= 1
    i += 1
print(temp)
