# 1712

def rotate(original):
    return list(zip(*original[::-1]))

a = [list(input()) for i in range(4)]
b = [list(input()) for i in range(4)]

for i in range(4):
    for x in range(4):
        for y in range(4):
            if a[x][y] == "X":
                print(b[x][y], end='')
    a = rotate(a)
