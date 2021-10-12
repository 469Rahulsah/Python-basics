#Created by Rahul kumar
#E-mail Id:- rahul12072002sah@gmail.com
num1 = int(input("starting number:"))
num2 = int(input("ending number:"))
sum = 0
flag = 0
for j in range(num1, num2):
    for i in range(2, j):
        if j%i == 0:
            flag = 1
            break
        else:
            flag = 0
    if flag==0:
        print(j)
        sum += j
        
print("summation is:",sum)
