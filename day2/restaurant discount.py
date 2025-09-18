bill=int(input("enter the total bill"))
if bill>1000:
    discount=bill*0.10
elif bill>500:
    discount=bill*0.5
else:
    discount=0
final_amount=bill=discount
print(f"original bill:{bill}")
print(f"discount:{discount}")
print(f"final amount to pay: {final_amount}")
