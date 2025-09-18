s = input()
alpha_count = sum(c.isalpha() for c in s)
digit_count = sum(c.isdigit() for c in s)
print(alpha_count, digit_count)