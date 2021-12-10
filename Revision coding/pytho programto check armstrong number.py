# Armstrong program
# Created by Rahul Kumar
num = int(input("Enter the number:"))
if num<10:
    print("No,it's not a armstrong number.")
elif num<=100:
    print("No,it's not a armstrong number.")
elif num<1000:
    a = num//100
    b = num%100
    c = b//10
    d = b%10
    e = a**3+c**3+d**3
    if num == e:
        print("Yes,it's a armstrong number.")
    else:
        print("No,it's not a armstrong number.")
elif num<10000:
    f = num//1000
    g = num%1000
    h = g//100
    i = g%100
    j = i//10
    k = i%10
    l = f**3+h**3+j**3+k**3
    if num == l:
        print("Yes,it's a armstrong number.")
    else:
        print("No,it's not a armstrong number.")
