#Python program for factorial of a number.
num = int(input("Enter the number:"))
count = 1
for i in range(1,num+1):
    count*= i
print(count)    
    
