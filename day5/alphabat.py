string=input("enter the string:")
alphabet,digit,specialchar=0,0,0
for ch in string:
    if ch.isalpha():
        alphabet+=1
    elif ch.isdigit():
        digit+=1
    else:
        specialchar+=1
print(f"count of alphabet charcters is{alphabet}")
print(f"count of digit is{digit}")
print(f"count of specialchar is{specialchar}")