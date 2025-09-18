num=int(input("enter the integer value:"))
factor=0
for i in range(1,num+1):
    if(num%i==0):
        factor+=1
res="prime number" if(factor==2) else "not a prime number"
print(f"{num} is {res}")