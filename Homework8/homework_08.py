lst = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]

def sum_of_index(list):
    result = []
    for element in list:
        nums = element.split(",")
        total = 0
        try:
            for num in nums:
                total += int(num)
            result.append(total)
        except Exception as error:
            result.append(f"Не можу це зробити! ({error})")
    return result

print (sum_of_index(lst))


