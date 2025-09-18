n = int(input("Enter number of elements: "))
numbers = list(map(int, input("Enter elements: ").split()))
print(*dict.fromkeys(numbers))