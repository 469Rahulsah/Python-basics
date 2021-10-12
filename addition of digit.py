#Created by Rahul kumar
#E-mail Id:- rahul12072002sah@gmail.com
num = int(input("Enter any number:"))
if num<100:
    c = (num//10)
    d = num%10
    print("The addition of number is:",c+d)
elif num<1000:
    e = num//100
    f = num%100
    g = f%10
    h = f//10
    print("The addition of number is:",e+g+h)
elif num<10000:
    i = num//1000
    j = num%1000
    k = j//100
    l = k%100
    m = l//10
    n = l%10
    print("The addition of number is:",i+k+m+n)

elif num<100000:
    i = num//10000
    j = num%10000
    print("The addition of number is:",i+j)

