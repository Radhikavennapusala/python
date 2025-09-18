n=int(input("enter the value of n:"))
rem,rev=0,0
temp=n
print(f"user entered number is{n}")
while(n!=0):
    rem=n%10
    rev=rev*10+rem
    n=n//0
print(f"reversed number is{rev}")
if(temp==rev):
    print("palindrome")
else:
    print("not a palindrome")
