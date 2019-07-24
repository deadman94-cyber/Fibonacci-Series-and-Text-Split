a = input("enter a string\t = ")
print (a)
print("Length of string =\t" , len(a))
for i in range (0,len(a)):
    print(a[i], "=" ,i)
print("\n now we will split the string")
for j in range (0,len(a)+1):
    print(a[0:j])
