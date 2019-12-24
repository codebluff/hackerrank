import statistics

n = int(input())

numbers = list(map(int, input().split()))

print(statistics.pstdev(numbers))