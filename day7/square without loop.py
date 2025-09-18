#second method
num=list(map(int,input("enter the number:").split()))
square=list(map(lambda i:i*i,num))
print(square)


#first  method
size=int(input("enter the size of list:"))
list=[]
new=[]
for i in range(size):
    val=int(input("enter the value:"))
    list.append(val)
print(list)
for i in list:
    i=i*i
    new.append(i)
print(new)
