#Created by Rahul kumar
#E-mail Id:- rahul12072002sah@gmail.com
num = int(input("Enter the number:"))
num2 = int(input("Enter the second number:"))
c = num*num2
for i in range(1,c):
    if num%i == 0 and num2%i == 0:
        p = i
print("The H.C.F is:",p)
