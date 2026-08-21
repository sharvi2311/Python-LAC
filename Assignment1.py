A = int(input("Enter number A = "))
B = int(input("Enter number B = "))
C = int(input("Enter number C = "))

# For all equal numbers
if (A==B==C):
    print("A,B,C are equal")
    
# For either of the numbers equal and lesser or greater than the 3rd number
elif(A==B or B==C or C==A):
    if(A==B and A>C):
        print("A and B are equal and greater than C")
    elif(B==C and B>A):
        print("B and C are equal and greater than A")
    elif(C==A and A>B):
        print("A and C are equal and greater than B")
    elif(A==B and A<C):
        print("A and B are equal and lesser than C")
    elif(A==C and A<B):
        print("A and C are equal and lesser than C")
    elif(B==C and B<A):
        print("B and C are equal and lesser than C")

# For each different number
elif (A>B and A>C):
    print("A is largest among three")
elif (B>A and B>C):
    print("B is largest among three")
else:
    print("C is largest among three")
