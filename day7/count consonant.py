s = input("Enter a string: ")
count = sum(1 for char in s.lower() if char.isalpha() and char not in 'aeiou')
print(count)