# -*- coding: utf-8 -*-
from random import randint
import simple_draw as sd


def snowfall_paint():
    N = 8
    # создание списка из N точек координат х с интервалом в 30 пикселей
    coordinate_x = {(n + 1) * 30 for n in range(N)}
    # создание словаря координат с параметрами факторов формы снежинок, объявление переменных для внесения изменений
    # в словарь в будущем, таких как изменение координаты у в меньшую сторону, значение самой координаты у, значение
    # смещения координаты х, непосредственные значения координаты х
    snow_form = {}
    for x in coordinate_x:
        factor_a = randint(4, 8) / 10
        factor_b = randint(25, 45) / 100
        factor_c = randint(50, 70)
        change_y = 0  # насколько уменьшается у при каждой итерации, будет изменено
        y = randint(450, 600)  # значение у по умолчанию, будет изменено
        z = 0  # отклонение координаты по х, будет изменено
        coord_x = x  # начальные координаты х, равные значению из списка. В цикле изменяется на величину z
        snow_form[x] = factor_a, factor_b, factor_c, change_y, y, z, coord_x

    def snowfall(size):
        y = 600
        while y >= 40:
            # организация выхода из бесконечного цикла
            if sd.user_want_exit():
                break
            for x in snow_form:
                # цикл для создания рандомных переменных для каждого х (в каждой итерации разные)
                factor_a = snow_form[x][0]
                factor_b = snow_form[x][1]
                factor_c = snow_form[x][2]
                change_y = randint(1, 2)  # значение ускорения падения у, меняется в цикле для разных значений
                y = snow_form[x][4]
                z = randint(-2, 2)  # значение отклонения х для имитации ветра. меняется в цикле для разных значений
                coord_x = snow_form[x][6] + z  # изменение координаты х на величину z
                snow_form[x] = factor_a, factor_b, factor_c, change_y, y, z, coord_x
            for x in snow_form:
                # цикл отрисовывания всех N снежинок по координатам из словаря с учетом смещений
                sd.start_drawing()
                factor_a = snow_form[x][0]
                factor_b = snow_form[x][1]
                factor_c = snow_form[x][2]
                change_y = snow_form[x][3]
                y = snow_form[x][4] - change_y
                z = snow_form[x][5]
                coord_x = snow_form[x][6]
                start_point = sd.get_point(coord_x, y)
                sd.snowflake(start_point, length=size, color=sd.COLOR_WHITE, factor_a=factor_a, factor_b=factor_b,
                             factor_c=factor_c)
                sd.finish_drawing()
                # sd.sleep(0.005)
                if y < 40:
                    # когда снежинка упала, перезаписать высоту отрисовки и форму снежинки, новая снежинка
                    y = randint(450, 600)
                    factor_a = randint(4, 8) / 10
                    factor_b = randint(25, 45) / 100
                    factor_c = randint(50, 70)
                    snow_form[x] = factor_a, factor_b, factor_c, change_y, y, z, coord_x
            if y >= 40:
                for x in snow_form:
                    # пока снежинка не упала, повторять отрисовку снежинки цветом фона, чтобы её стирать с предыдущей
                    # позиции

                    factor_a = snow_form[x][0]
                    factor_b = snow_form[x][1]
                    factor_c = snow_form[x][2]
                    change_y = snow_form[x][3]
                    y = snow_form[x][4] - change_y
                    z = snow_form[x][5]
                    coord_x = snow_form[x][6]
                    start_point = sd.get_point(coord_x, y)
                    sd.snowflake(start_point, length=size, color=sd.background_color, factor_a=factor_a,
                                 factor_b=factor_b,
                                 factor_c=factor_c)
                    snow_form[x] = factor_a, factor_b, factor_c, change_y, y, z, coord_x

    snowfall(randint(20, 30))
