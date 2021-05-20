# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join
new_list = []
# TODO здесь ваш код
def district_citizens(folks,new_list):
    district_citizens_string = ", ".join(folks)
    new_list += district_citizens_string + "\n"
    return new_list

from district.central_street.house1.room1 import folks
district_citizens(folks, new_list)

from district.central_street.house1.room2 import folks
district_citizens(folks, new_list)

from district.central_street.house2.room1 import folks
district_citizens(folks, new_list)

from district.central_street.house2.room2 import folks
district_citizens(folks, new_list)

from district.soviet_street.house1.room1 import folks
district_citizens(folks, new_list)

from district.soviet_street.house1.room2 import folks
district_citizens(folks, new_list)

from district.soviet_street.house2.room1 import folks
district_citizens(folks, new_list)

from district.soviet_street.house2.room2 import folks
district_citizens_string = ", ".join(folks)
new_list += district_citizens_string

for symbol in new_list:
    print(symbol, end="")

