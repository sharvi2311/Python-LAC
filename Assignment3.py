def triangle():
    a=int(input("Enter side 1 = "))
    b=int(input("Enter side 2 = "))
    c=int(input("Enter side 3 = "))

    if(a==b==c):
        print("Equilateral triangle")
    elif (a==b or b==c or c==a):
        print("Isosceles triangle")
    else:
        print("Scalene triangle")

triangle()
