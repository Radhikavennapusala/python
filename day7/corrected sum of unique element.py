n = int(input())
numbers = list(map(int, input().split()))
unique_sum = sum(num for num in set(numbers) if numbers.count(num) == 1)
print(unique_sum)