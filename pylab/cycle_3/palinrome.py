number=input("Enter a number : ")
is_palin=True
length = len(number)

for i in range(length//2):
	if number[i]!=number[length -1-i]:
		is_palin=False
		break
if is_palin:
	print(f"{number} is a palindrome number")
else:
	print(f"{number} is not a palindrome number")
