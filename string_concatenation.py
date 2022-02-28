st = input("Enter the first string:")
st1 = input("Enter the second string:")
st2 = st+st1
count = 0
d = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i in st2:
    if i in d:
        count+=1
    else:
        pass
if count == 26:
    print("Yes")
else:
    print("Concatenation of the string are not equal to the abcd letters. ")
