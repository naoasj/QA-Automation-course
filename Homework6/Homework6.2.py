

h_1_to_find = "h"
h_2_to_find = "H"

while True:
    your_inp = input ('Введіть слово з h: ')
    found = False
    for h_char in your_inp:
        if h_char == h_1_to_find or h_char == h_2_to_find:
            found = True
            break
    if found:
        break







