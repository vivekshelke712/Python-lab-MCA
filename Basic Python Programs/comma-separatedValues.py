values = input("Enter comma-separated values: ")  


values_list = values.split(",")  
values_tuple = tuple(values_list)  

print("List:", values_list)  
print("Tuple:", values_tuple)
