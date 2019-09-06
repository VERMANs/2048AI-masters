x = 4
y = 9
numX = 0
numY = 0
sum = []
n = int(input())
if n % 9 == 0:
    sum.append(n // 9)
else:
    for i in range(0, n // 9 + 1):
        n1 = i
        if (n - i * y) % x == 0:
            n1 += (n - i * y) // x
            sum.append(n1)
if len(sum) != 0:
    print(min(sum), end="")
else:
    print(-1, end="")
