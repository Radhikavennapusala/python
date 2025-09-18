age=int(input("enter the age"))
if age<=5:
    print("free")
elif age>=5 and age<=12:
    print("half ticket")
elif age>=13 and age<=59:
    print("full ticket")
else:
    print("30% senior citizen discount")