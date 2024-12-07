import math
print("Quadratic equaion ax^2+bx+c")
a=float(int(input("Enter value a : ")))
b=float(int(input("Enter value b : ")))
c=float(int(input("Enter value c : ")))
desr=(b*b)-(4*a*c)
if(desr==0):
	print("Only one root value\n")
	ans=(-b)/2*a
	print("x =",ans)
elif(desr>0):
	sqrtvalue=math.sqrt(desr)
	ansone=(-b+sqrtvalue)/2*a
	anstwo=(-b-sqrtvalue)/2*a
        print("Roots are real and not equal")
	print("x1 = ",ansone)
	print("x2 = ",anstwo)
else:
	print("Complex Root !!")
	sqrtvalue=math.sqrt(abs(desr))/(2*a)
	print(-b/(2*a),"+i",sqrtvalue)
	print(-b/(2*a),"-i",sqrtvalue)
