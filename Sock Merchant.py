
def sockMerchant(n, ar):
    ar.sort()
    count = 0
    skip = []
    # lets print pairs
    for i in range(0, len(ar) - 1):
        if i not in skip:
            if ar[i] == ar[i + 1]:
                skip.append(i)
                skip.append(i+1)
                count += 1
    return count


n = int(input())

ar = list(map(int, input().rstrip().split()))

print(sockMerchant(n, ar))
