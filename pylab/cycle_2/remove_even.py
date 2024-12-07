list=input("ENTER A INTEGER VALUE (SEPERATED BY COMMA) : ").split(",")
list=[int(x)for x in list]
remove=[i for i in list if i%2!=0]
print("ORGINAL LIST : ",list)
print("NEW LIST WITHOUT EVEN NUMBER : ",remove)
