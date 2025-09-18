s = input().strip()
vowels = set('aeiouAEIOU')
print(sum(1 for ch in s if ch in vowels))
