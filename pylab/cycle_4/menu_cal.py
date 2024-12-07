def add(x,y):
	return x+y
def substract(x,y):
	return x-y
def multiply(x,y):
	return x*y
def divide(x,y):
	if y!=0:
		return x/y
	else:
	        return "Error! Division by zero"
def modulus(x,y):
	return x%y

def calculator():
	while True:
		print("\nSelect operation : ")
		print("1.Add")
		print("2.Substruct")
		print("3.Multiply")
		print("4.Divide")
		print("5.Modulus")
		print("6.Exit...")

		choice=input("Enter choice (1/2/3/4/5/6) : ")

		if choice =='6':
			print("Exiting the calculator,Goodbye!!")
			break

		try:
			num1=float(input("Enter first number : "))
			num2=float(input("Enter second  number : "))

		except ValueError:
			print("Invalid input!Please enter numberic values:")
			continue
		if choice=='1':
			print(f"{num1}+{num2}={add(num1,num2)}")
		elif choice=='2':
			print(f"{num1}-{num2}={substract(num1,num2)}")
		elif choice=='3':
			print(f"{num1}*{num2}={multiply(num1,num2)}")
		elif choice=='4':
			print(f"{num1}/{num2}={divide(num1,num2)}")
		elif choice=='5':
			print(f"{num1}%{num2}={modulus(num1,num2)}")
		else:
			print("invalid input! please select a valid operation")
calculator()
