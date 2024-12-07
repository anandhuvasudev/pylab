x=[]
values=input("enter alist of integer (comma seperated) : ").split(",")
for i in values:
	if int(i)>100:
		x.append("over")
	else:
		x.append(int(i))
print(x)

