# -*- coding: utf-8 -*-

# Создать модуль my_burger. В нем определить функции добавления инградиентов:
#  - булочки
#  - котлеты
#  - огурчика
#  - помидорчика
#  - майонеза
#  - сыра
# В каждой функции выводить на консоль что-то вроде "А теперь добавим ..."

# В этом модуле создать рецепт двойного чизбургера (https://goo.gl/zA3goZ)
# с помощью фукций из my_burger и вывести на консоль.

# Создать рецепт своего бургера, по вашему вкусу.
# Если не хватает инградиентов - создать соответствующие функции в модуле my_burger

def standard_burger():
    import my_burger
    my_burger.bread()
    my_burger.tomato()
    my_burger.cutlet()
    my_burger.cucumber()
    my_burger.mayo()
    my_burger.bread()
    print("Стандартный бургер готов!")


def double_cheezeburger():
    import my_burger
    my_burger.bread()
    my_burger.cheeze()
    my_burger.tomato()
    my_burger.cutlet()
    my_burger.cucumber()
    my_burger.cutlet()
    my_burger.mayo()
    my_burger.cheeze()
    my_burger.bread()
    print("Двойной чизбургер готов!")


double_cheezeburger()
standard_burger()
