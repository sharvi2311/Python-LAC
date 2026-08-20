a = int(input("Enter number A = "))
b = int(input("Enter number B = "))
c = int(input("Enter number C = "))

if (a==b==c):
    print("A,B,C are equal")
elif(a==b or b==c or c==a):
    if(a==b and a>c):
        print("A and B are equal and greater than C")
    elif(b==c and b>a):
        print("B and C are equal and greater than A")
    elif(c==a and a>b):
        print("A and C are equal and greater than B")
    elif(a==b and a<c):
        print("A and B are equal and greater than C")
    elif(b==c and b<a):
        print("B and C are equal and greater than C")
    elif(a==c and a<b):
        print("A and C are equal and greater than C")
elif (a>b and a>c):
    print("A is largest among three")
elif (b>a and b>c):
    print("B is largest among three")
else:
    print("C is largest among three")
