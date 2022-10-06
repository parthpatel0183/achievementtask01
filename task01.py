print("what do you want to calculate 1. Area of circle 2. Area of triangle 3. Area of rectangle 4. perimeter of circle 5. perimeter of triangle 6. perimeter of rectangle")
choice = input("type 1,2,3,4,5,6")
if choice == '3':
    length=int(input("enter length of the rectangle"))
    breadth=float(input("enter the breadth of the rectangle"))
    area = length*breadth
    print("area of rectangle"+ str(area))
    

elif choice == '1':
    radius=float(input("radius"))
    area = 3.14*radius*radius
    print("area of the circle is"+ str(area))

elif choice =='3':
    length=int(input("length"))
    breadth=int(input("breadth"))
    perimeter=2*(length*breadth)
    print("perimeter of rectangle"+ str(perimeter))

elif choice =='4':
    radius=float(input("radius"))
    perimeter=2*3.14*radius
    print("perimeter of circle"+ str(perimeter))

elif choice=="2":     
    altitude=int(input("altitude"))
    base=int(input("base"))
    area=0.5*base*altitude
    print("area of triangle"+ str(area))
    

elif choice=="5":
    altitude=int(input("altitude"))
    base=int(input("base"))
    side=int(input("side"))
    perimeter=altitude*base*side
    print("perimeter of triangle"+ str(perimeter))

else:
    print("invalid choice")
