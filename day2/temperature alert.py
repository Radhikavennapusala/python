temp=int(input("enter the temp:"))
if temp<0:
    print("freezing weather")
elif temp>=0 and temp<=20:
    print("cold weather")
elif temp>=20 and temp<=35:
    print("normal weather")
else:
    print("hot weather")