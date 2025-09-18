n = int(input().strip())
arr = list(map(int, input().split()))
unique = sorted(set(arr), reverse=True)
if len(unique) >= 2:
    print(unique[1])
else:
    print(unique[0])

