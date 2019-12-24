n = int(input())

X = list(map(int, input().split()))
W = list(map(int, input().split()))

num = 1
den = 0
for i in range(n):
    num += (X[i] * (W[i]))
    den += W[i]
    print(num, den)

print(round(num/den, 1))
print(num / den)
