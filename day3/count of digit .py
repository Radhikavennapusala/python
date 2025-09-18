n=int(input("enter the value of n"))
digit_count = 0
while(n!=0):
    n=n//10
    digit_count+=1
print(f"digit_count is {digit_count}")