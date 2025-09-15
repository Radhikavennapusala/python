num1=int(input("enter the first integer"))
num2=int(input("enter the second integer"))
num3=int(input("enter the third integer"))
#if_else
smallest=num1 if (num1<num2 and num2<num3) else num2
res=num3 if(num3<num1 and num3<num2) else smallest
print(f"{res} is the smallest number")