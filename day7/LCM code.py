a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
lcm = (a * b) // gcd(a, b)
print(lcm)

