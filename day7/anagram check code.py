s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
print("YES" if sorted(s1.lower()) == sorted(s2.lower()) else "NO")