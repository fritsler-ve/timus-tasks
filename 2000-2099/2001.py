2001
sum1, sum2 = list(map(int, input().split()))
full1, empty2 = list(map(int, input().split()))
empty1, full2 = list(map(int, input().split()))
print(sum1 - empty1, sum2 - empty2)
