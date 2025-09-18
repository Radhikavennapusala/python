size=int(input("enter the size of list"))
char=[]
for i in range(size):
    element=input("enter alphabatic charcter {i+1}:")
    char.append(element)
print(f"user entered list:",char)
print(f"sorted list:",sorted(char))
