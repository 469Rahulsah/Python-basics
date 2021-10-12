#Created by Rahul kumar
#E-mail Id:- rahul12072002sah@gmail.com
num = int(input("Enter the number:"))
num2 = int(input("Enter the second number:"))
g = num2*num2
for i in range(1,g,1):
    if i%num == 0 and i%num2 == 0:
        break
print("The LCM is:",i)
    
    
