def repeatedString(s, n):
    count = 0
    for c in s:
        count += 1
    cnt = s.count('a')
    ans = int((n / count) * cnt)
    return ans


s = input()

n = int(input())

print(repeatedString(s, n))
