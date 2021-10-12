#Created by Rahul kumar
#E-mail Id:- rahul12072002sah@gmail.com
num = int(input("Enter the number:"))
if num<100:
    a = num//10
    b = num%10
    c = (a**3)+(b**3)
    if c == num:
        print("It is an armstrong.")
    else:
        print("It is not an armstrong number.")
if num<1000:
    d = num//100
    e = num%100
    f = e//10
    g = e%10
    h = (d**3)+(f**3)+(g**3)
    if h == num:
        print("It is an armstrong.")
    else:
        print("It is not an armstrong number.")
    

    
