# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    multiplier = 1

    while True:
        result = number * multiplier
        if result >= 25:
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))
        multiplier += 1

    return result

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
number1 = int (input ("Введіть перше число "))
number2 = int (input ("Введіть друге число "))

def sum_numbers (number1, number2):
    num = sum ([number1, number2])
    return num

result = sum_numbers (number1, number2)
print (result)

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
lst = [1,2,3,4,5]

def list_sum (lst):
    lst_sum = 0
    for i in lst:
        lst_sum = i + lst_sum
    avg = lst_sum / len(lst)
    return avg

result = list_sum (lst)

print (result)

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
inpt = input ("Введіть строку: ")


def reverced_str (inpt):
    rvrcd_lst = []
    for element in inpt:
        rvrcd_lst.insert(0, element)
    return "".join(rvrcd_lst)

result = reverced_str (inpt)

print (result)

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
lst = ["Написати", "функцію", ",", "яка", "приймає", "список", "слів","Абракадабра"]

def long_string (lst):

    longest_word = max(lst, key=len)

    return longest_word

result = long_string (lst)

print (result)

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    return str1.find(str2)

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7
#Завдання 6.1 порахувати к-сть унікальних елементів в строці
def string_unique_element_count (item):
    unique_element = set(item)
    count = len(unique_element)
    return count >= 10

item = "1234567890-qwertyyifdsa"
result = string_unique_element_count (item)
print (result)


# task 8
#Завдання 6.3 забрати в новий список стоки
def take_stringf_from_list (item):
    lst2 = []
    for element in item:
        if isinstance(element, str):
            lst2.append(element)
    return lst2

item = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
result = take_stringf_from_list (item)
print (result)

# task 9
#Завдання 4.5 скільки слів у тексті починається з Великої літери
def amount_of_string_from_capital (item):
    lst = item.split()
    count = 0
    for word in lst:
        if word.istitle():
            count = count + 1
    return count

item = "Якась Строка з Домашньго завдання"
result = amount_of_string_from_capital (item)
print (result)

# task 10
#Завдання 6.4 посумувати парні числа в списку
def sum_of_even_elements (item):
    lst2 = []
    for element in item:
        if element % 2 == 0:
            lst2.append(element)
    lst2_sum = sum (lst2)
    return lst2_sum 

item = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
result = sum_of_even_elements (item)
print (result)

"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""