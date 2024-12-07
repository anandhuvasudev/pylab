list1_input=input("ENTE THE FIRST LIST OF INTEGER (COMMA SEPERATED)\n")
list1=[int(num.strip())for num in list1_input.split(",")]
list2_input=input("ENTER THE SECOND LIST OF INTEGER (COMMA SEPERATED)")
list2=[int(num.strip())for num in list2_input.split(",")]

same_length=len(list1)==len(list2)
same_sum=sum(list1)==sum(list2)
common_values=any(num in list2 for num in list1)
print("ARE THE LIST OF THE SAME LENGTH ?",same_length)
print("DO THE LIST SUM TO THE SAME VALUES ?",same_sum)
print("Is there any values that occur in both lists ?",common_values)
