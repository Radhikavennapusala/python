num=int(input("enter the integer"))
#if_else
if(num>=-9 and num<=9):
   print("digit")
else:
     print("number")
#ternary operator
res="digit" if(num>=-9 and num<=9) else "number"
print(res)