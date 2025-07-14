my_string = input("Введіть стороку: ")
unique_element = set(my_string)
count = len(unique_element)
if count >= 10:
    print (True)
else:
    print (False) 