total = 0
for i in range(100,1000):
    if str(i)==str(i)[::-1]:
        print(i)
        total += i
print("sum:",total)
