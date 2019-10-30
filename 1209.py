# 1209

def value(number):
    return int((1 + (1 + 8 * number)**0.5) / 2) - 1


def nvalue(number):
    return int(((number + 1) * number) / 2)


def solve(number):
    if number == 1:
        return 1
    if (nvalue(value(number)) == number - 1):
        return 1
    return 0


res = []
N = int(input())
for i in range(N):
    a = int(input())
    res.append(str(solve(a)))
print(' '.join(res))