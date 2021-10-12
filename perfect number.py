#Created by Rahul kumar
#E-mail Id:- rahul12072002sah@gmail.com
num = int(input("Enter the number:"))
dam = 0
for i in range(1,num,1):
    if num%i == 0:
        print(i)
        dam+=i
print("Addition of this is",dam)
if dam == num:
    print("It is a perfect number.")
else:
     print("It is not a perfect number.")
    
