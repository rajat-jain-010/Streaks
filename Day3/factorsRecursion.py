def Prime_Factorial(n, arr):
    if n < 4:
        return n
    for i in range(2, int(2+n//2)):
        if i == (1 + n // 2):
            arr.append(n)
            n = 1
            return
        if n % i == 0:
            arr.append(i)
            n = n // i
            Prime_Factorial(n, arr)
            break
    return arr


n = 1542
arr = []
print(Prime_Factorial(n, arr))