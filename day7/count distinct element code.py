n = int(input())
numbers = list(map(int, input().split()))
distinct_count = len(set(numbers))
print(distinct_count)
