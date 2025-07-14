lst1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

lst2 = []

for element in lst1:
    if element % 2 == 0:
        lst2.append(element)

lst2_sum = sum (lst2)

print (lst2_sum)