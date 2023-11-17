def cuboid():
    l=(int(input("enter the length :")))
    b=(int(input("enter the breadth :")))
    h=(int(input("enter the height :")))
    area=2*(l*b+b*h+h*l)
    peri=4*(l+b+h)
    print("area of cuboid is",area)
    print("perimeter of cuboid is",peri)
