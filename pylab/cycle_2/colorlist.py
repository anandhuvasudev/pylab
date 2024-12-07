color_list1 = input("Enter the first list of colors (comma-separated): ").split(",")
color_list2 = input("Enter the second list of colors (comma-separated): ").split(",")

list1 = [item.strip() for item in color_list1]  
list2 = [item.strip() for item in color_list2]
result = [item for item in list1 if item not in list2]

print("Values from color_list1 not contained in color_list2:", result)
