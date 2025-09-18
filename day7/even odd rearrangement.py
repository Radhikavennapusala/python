n=input().split()
even=[]
odd=[]
for i in n:
    n=int(i)
    if n%2==0:
        even.append(i)
    else:
        odd.append(i)
e=sorted(even)
o=sorted(odd)
print(even+odd)
