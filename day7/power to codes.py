n = int(input("Enter a number: "))
print("YES" if n > 0 and (n & (n-1)) == 0 else "NO")
