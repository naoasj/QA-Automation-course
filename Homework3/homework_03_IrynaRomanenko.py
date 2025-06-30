# alice_in_wonderland = '"Would you tell me, please, which way I ought to go from here?"\n"That depends a good deal on where you want to get to," said the Cat.\n"I don't much care where ——" said Alice.\n"Then it doesn't matter which way you go," said the Cat.\n"—— so long as I get somewhere," Alice added as an explanation.\n"Oh, you're sure to do that," said the Cat, "if you only walk long enough."'

# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк
alice_in_wonderland = ('''Would you tell me, please, which way I ought to go from here?"
    "That depends a good deal on where you want to get to," said the Cat.
    "I don\'t much care where ——" said Alice.
    "Then it doesn\'t matter which way you go," said the Cat.
    "—— so long as I get somewhere," Alice added as an explanation.
    "Oh, you\'re sure to do that," said the Cat, "if you only walk long enough.''')

print(alice_in_wonderland)

"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
azov_sea = 37800
black_sea = 436402

total = (azov_sea + black_sea)

print (f'Разом Азовське та Чорне море займають {total} км2')

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
total = 375291
sklad_1and2 = 250449
sklad_2and3 = 222950

sklad_3 = total - sklad_1and2

sklad_1 = sklad_2and3 - sklad_3

sklad_2 = (total - (sklad_1 + sklad_3))

print('''На першому складі {sklad_1} товару. 
На другому складі {sklad_2} товару. 
На третьому складі {sklad_3} товару.''')

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
month_payment = 1179
period = 12 + 6 

total_PC = ( month_payment * period)

print (f'Вартість комп\'ютера {total_PC} грн')

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
a = 8019 % 8
b = 9907 % 9
c = 2789 % 5
d = 7248 % 6
e = 7128 % 5
f = 19224 % 9

print ("a =", a,
       "b =", b,
       "c =", c,
       "d =", d,
       "e =", e,
       "f =", f)

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
pizza_big = 274 
pizza_medium = 218
juice = 35
cake = 350 
water = 21 

sum = (pizza_big * 4) + (pizza_medium * 2) + (juice * 4) + cake + (water * 3)
print (sum)
# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
photo = 232
amount_per_page = 8

total_pages = photo // amount_per_page

print (f'{total_pages} cторінок')

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?

"""
distance_total = 1600
distance_100 = 100
amount_per_100 = 9
full_back = 48

total_amount = (distance_total * amount_per_100)//distance_100

recharge = total_amount // full_back


print (f'1. {total_amount} бензину треба щоб доїхати. 2. Заправлятись треба {recharge} рази.')
