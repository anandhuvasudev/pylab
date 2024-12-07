my_dict={'banana':3,'apple':5,'orange':2,'kiwi':4}
keys_asc=dict(sorted(my_dict.items()))
print("Sorted by keys (ascending): ",keys_asc)

keys_desc=dict(sorted(my_dict.items(),reverse=True))
print("sorted by keys (descenting): ",keys_desc)

value_asc=dict(sorted(my_dict.items(),key=lambda items:items[1]))
print("Sorted by values (ascending):",value_asc)

value_desc=dict(sorted(my_dict.items(),key=lambda items:items[1],reverse= True))
print("Sorted by values (descending):",value_desc)

