#Created by Rahul kumar
#E-mail Id:- rahul12072002sah@gmail.com
num = int(input("Enter the first number:"))
flag = 0
for i in range(2, num):
    if num%i==0:
        flag = 1
        break
if flag == 1:
    print("The given number is not a prime number")
else:
    print("The given number is a prime number")
