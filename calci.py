#calculator programme python CS lab project
w=int(input('Start??(y=1/n=0):'))
while w==1:
    n=int(input('Enter \n1.for addition\n2.for subtraction\n3.for multiplication\n4.for division\n5.for simple interest\n6.for trignometric functions\n7.simple math functions\n8.conversion\n9.Areas\n10.Volume\n='))
    i=0
    import math
    if n==1:
        e=int(input('Enter the no of nos to be added:'))
        f=int(input('Enter the first number:'))
        s=0+f
        for i in range(0,e-1):
            r=int(input('Enter:'))
            s=s+r
            print(s)
        print('The sum is :',s)
    
    elif n==2:
        e=int(input('Enter the no of nos to be subtracted:'))
        f=int(input('Enter the first number:'))    
        s=0+f
        for i in range(0,e-1):
            r=int(input('Enter:'))
            s=s-r
            print(s)
        print('The result is :',s)
    elif n==3:
        e=int(input('Enter the no of nos to be multiplied:'))
        f=int(input('Enter the first number:'))
        s=0+f
        for i in range(0,e-1):
            r=int(input('Enter:'))
            s=s*r
            print(s)
        print('The result is :',s)
    elif n==4:
        e=int(input('Enter the no of nos to be divided:'))
        f=int(input('Enter the first number:'))
        s=0+f
        for i in range(0,e-1):
            r=int(input('Enter:'))
            s=s/r
            print(s)
        print('The result is :',s)
    elif n==5:
        si=0
        a1=int(input('Enter principal:'))
        a2=int(input('Enter rate of interest:'))
        a3=int(input('Enter time:'))
        si=(a1*a2*a3)/100
        print('Simple interest is:',si)
    elif n==6:
        k=int(input('Enter \n1.for sin(x)\n2.for cos(x)\n3.for tan(x)\n4.for sec(x)\n5.for cosec(x)\n6.for cot(x)\n='))
        x=float(input('Enter the value of x (in radians):'))
        import math
        if k==1:
            r=math.sin(x)
            print('Sin(',x,') is=',r)
        if k==2:
            r=math.cos(x)
            print('Cos(',x,') is=',r)
        if k==3:
            r=math.tan(x)
            print('Tan(',x,') is=',r)
        if k==4:
            r=math.sec(x)
            print('Sec(',x,') is=',r)
        if k==5:
            r=math.cosec(x)
            print('Cosec(',x,') is=',r)
        if k==6:
            r=math.cot(x)
            print('Cot(',x,') is=',r)
    elif n==7:
        k=int(input('Enter \n1.for GCD function\n2.for squareroot\n3.factorial\n4.ceiling \nfunctions ='))
        if k==1:
            x=int(input('Enter x:'))
            y=int(input('Enter y:'))
            r=math.gcd(x,y)
            print('GCD(',x,y,') is=',r)
        if k==2:
            x=int(input('Enter x:'))
            r=math.sqrt(x)
            print('squareroot(',x,') is=',r)
        if k==3:
            x=int(input('Enter the number:'))
            r=math.factorial(x)
            print('Factorial(',x,') is=',r)
        if k==4:
            x=int(input('Enter the number:'))
            r=math.ceil(x)
            print('Ceil(',x,') is=',r)
    elif n==8:
        k=int(input("Enter \n1.for in degrees\n2.for in radians\n="))
        if k==1:
            x=float(input('Enter in radians:'))
            r=math.degrees(x)
            print('Degrees(',x,') is=',r)
        if k==2:
            x=float(input('Enter in degrees:'))
            r=math.radians(x)
            print('Radians(',x,') is=',r)
    elif n==9:
        c=int(input('Enter the no of the shape whose area you would like to find out\n1.triangle\n2.rectangle\n3.circle\n4.square\n5.rhombus\n6.trapezium\n7.cube\n8.cuboid\n9.cylinder\n10.cone:'))
        if c==1:
            b=int(input('Enter the first side:'))
            v=int(input('Enter thr second side:'))
            u=int(input('Enter the third side:'))
            s=(b+u+v)/2
            print('The area of the triangle is:',(s*(s-b)*(s-v)*(s-u))**0.5)
        elif c==2:
            b=int(input('Enter the first side:'))
            v=int(input('Enter the second side:'))
            print('The area of the rectangle is:',b*v)
        elif c==3:
            b=int(input('Enter the radius:'))
            print('The area of the circle is:',3.14*b*b)
        elif c==4:
             b=int(input('Enter the side:'))
             print('The area of the square is:',b*b)
        elif c==5:
             b=int(input('Enter the side:'))
             v=int(input('Enter the height:'))
             print('The area of the rhombus is:',a*h)
        elif c==6:
             b=int(input('Enter the first parallel side:'))
             v=int(input('Entre the second parallel side:'))
             u=int(input('Enter the height:'))
             print('The area of the trapzium is:',0.5*(b+v)*u)
        elif c==7:
             b=int(input('Enter the side:'))
             print('The area of the cube:',6*a*b)
        elif c==8:
             b=int(input('Enter the first side:'))
             s=int(input('Enter the second side:'))
             e=int(input('Enter the height:'))
             print('The area of the cuboid is:',2(s*b+b*e+b*e))
        elif c==9:
            b=int(input('Enter the radius:'))
            s=int(input('Enter the height:'))
            print('The area of the cylinder is:',3.14*b*b*s)
        elif c==10:
            b=int(input('Enter the radius:'))
            v=int(input('Enter the slant height:'))
            print('The area of the cone is:',3.14*(b+v))
    elif n==10:
        c=int(input('Enter the no of the shape you would ike to find out\n1.Cube\n2.cuboid\n3.cone\n4.sphere\n5.Triangular prism\n=:'))
        if c==1:
            a=int(input('Enter the side:'))
            print('The volume of the cube is:',a*a*a)
        elif c==2:
            b=int(input('Enter the first side:'))
            s=int(input('Enter the second side:'))
            e=int(input('Enter the height:'))
            print('The volume of the cuboid is:',b*s*e)
        elif c==3:
            b=int(input('Enter the radius:'))
            h=int(input('Enter the height:'))
            print('The volume of the cone is:',((3.14*b*b*h)/3))
        elif c==4:
            b=int(input('Enter the radius:'))
            print('The volume of the radius is:',((4*3.4*b*b*b)/3))
        elif c==5:
            b=int(input('Enter the height of the prism:'))
            h=int(input('Enter the side of the prism:'))
            print('The volume of the prism is:',(math.sqrt(3)*h*h*b))
