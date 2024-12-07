str=input("Enter a String :")
if str[-3:]=="ing":
	str=str[:-3]+"ly"
else:
	str=str+"ing"
print("Modified string ",str)
