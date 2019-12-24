def median(a, l, r):
    n = r - l + 1
    n = (n + 1) // 2 - 1
    return n + l
def IQR(a, n):

    # Index of median of entire data
    mid_index = median(a, 0, n)

    # Median of first half
    Q1 = a[median(a, 0, mid_index)]

    # Median of second half
    Q3 = a[median(a, mid_index + 1, n)]

    # IQR calculation
    return (Q3 - Q1)

n = int(input())
x = sorted(list(map(int, input().split())))
print(IQR(x, n))
