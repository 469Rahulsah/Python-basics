#Created by Rahul kumar
#E-mail Id:- rahul12072002sah@gmail.com
print('''Please enter the number between 10 to 1000
and do not enter the digit with zero.''')
num = int(input("Enter the number:"))
if num<100:
    a = (num//10)
    b = (num%10)
    print("The reverse of a number is:",(b*10)+(a))
elif num<1000:
    c = (num//100)
    d = (num%100)
    e = (d//10)
    f = (d%10)
    print("The reverse of a number is:",(f*100)+(e*10)+(c))
