s = input()
vowels = 'aeiouAEIOU'
result = ''.join([char for char in s if char not in vowels])
print(result)