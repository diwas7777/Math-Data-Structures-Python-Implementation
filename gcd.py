from calculate import GCD

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

while GCD(a,b) != 0:
    tempR = GCD(a,b)
    a, b = b, tempR

print("Greatest Common Divisor: ", tempR)