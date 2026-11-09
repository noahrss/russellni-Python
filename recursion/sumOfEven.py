def sumEven():
    if n % 2 != 0:
        n = n + 1
    if n < 1:
        return 0
    return n + sumEven(n-1)

print(sumEven(6))