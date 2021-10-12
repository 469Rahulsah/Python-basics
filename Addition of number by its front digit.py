#Created by Rahul kumar
#E-mail Id:- rahul12072002sah@gmail.com
num = int(input("Enter the last term of list:"))
a = 0
b = 1
print(a)
print(b)
for i in range(0,num+1):
    c = a+b
    a = b
    b = c
    print(c)
