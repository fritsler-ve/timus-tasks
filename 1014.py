def solve(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1

    result = 0
    power = 1

    for divider in range(9, 1, -1):
        while number % divider == 0:
            if number == 1:
                break
            result += power * divider
            power *= 10
            number //= divider
    if number == 1:
        return result
    return -1


print(solve(int(input())))
