n=int(input("Enter the numbeer of name: "))
names=[]
for i in range(n):
	name=input("Enter First name : ")
	names.append(name)
	count=0
for name in names:
	for ch in name:
		if ch=="a":
			count+=1
print("total occurance of a : ",count)

