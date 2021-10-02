P = float(input("Enter Principal amount: "))
r = float(input("Enter Rate: "))
t = int(input("Enter time: "))

a = P * (pow((1 + r / 100), t))
ci = a - P
print("Compound interest is", ci)