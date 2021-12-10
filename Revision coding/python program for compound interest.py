# Compound interest
# Created by Rahul Kumar
num = float(input("Enter the principal:"))
num2 = float(input("Enter the rate:"))
num3 = float(input("Enter the time:"))
d = num2/100
e = 1+d
f = e**num3
g = f*num
h = g - num
print("Compound interest:",h)
