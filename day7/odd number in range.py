l,r=map(int,input("enter two number:").split())
print(*[i for i in range(l,r+1) if i%2!=0])