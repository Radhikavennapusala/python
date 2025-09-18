#first method
n=int(input())
n=list(str())
x=n.count('3')
y=n.count('7')
print(x+y)

#second method
n=input().strip()
print(sum(1 for d in n if d in ['3','7']))