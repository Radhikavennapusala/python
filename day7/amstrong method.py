n = int(input("Enter a number: "))
temp = n
sum = 0
while temp != 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
print("YES" if sum == n else "NO")

