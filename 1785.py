def getAmount(n):
    if n < 5:
        return "few"
    if n < 10:
        return "several"
    if n < 20:
        return "pack"
    if n < 50:
        return "lots"
    if n < 100:
        return "horde"
    if n < 250:
        return "throng"
    if n < 500:
        return "swarm"
    if n < 1000:
        return "zounds"
    return "legion"

print(getAmount(int(input())))
