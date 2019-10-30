N = list(map(int, list(input())))
if (sum(N[0 : 3]) - sum(N[3 : 6]) == 1 and N[5] != 9) or (sum(N[0 : 3]) - sum(N[3 : 6]) == -1 and N[5] != 0):
    print("Yes")
else:
    print("No")
