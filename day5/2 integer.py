a=int(input("enter the  value of first integer"))
b=int(input("enter the value of second integer"))
#first logic
a=a+b
b=a-b
a=a-b
print("after swapping")
print(f"a={a}")
print(f"b={b}")

#second logic(temporary variable)
temp=a
a=b
b=temp
print("after swapping")
print(f"a={a}")
print(f"b={b}")

#third logic
a,b=b,a
print("after swapping")
print(f"a={a}")
print(f"b={b}")

