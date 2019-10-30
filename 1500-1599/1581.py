n = int(input())
arr = list(map(int, input().split()))
current_num = arr[0]
current_amount = 1
for i in range(1, n):
    if arr[i] == current_num:
        current_amount += 1
    else:
        print(current_amount, current_num, end=' ')
        current_num = arr[i]
        current_amount = 1
print(current_amount, current_num)
