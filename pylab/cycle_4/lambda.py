area_of_square=lambda side : side*side
area_of_rectangle=lambda length,width:length*width
area_of_triangle=lambda base,height:0.58 *base*height

side=int(input("Enter side"))
length=int(input("enter length"))
width=int(input("enter width "))
base=int(input("enter base "))
height=int(input("enter height "))
print(f"Area of square : {area_of_square(side)}")
print(f"Area of rectangle : {area_of_rectangle(length,width)}")
print(f"Area of triagnle : {area_of_triangle(base,height)}")
