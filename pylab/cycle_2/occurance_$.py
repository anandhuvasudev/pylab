str = input("Enter a string\n")
fchar=str[0]
str=str.replace(fchar,"$")   
str=fchar+str[1:]
print(str)
