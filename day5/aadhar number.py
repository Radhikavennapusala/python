aadhar=input("enter the 12-digit aadhar number:")
hidden="*" * 8 + aadhar[-4:]
print(f"masked aadhar number:",{hidden})