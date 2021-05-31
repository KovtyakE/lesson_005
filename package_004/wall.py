# -*- coding: utf-8 -*-

import simple_draw as sd


def wall_paint():
    # счетчик для определения сдвига, нужно ли сдвигать начало и конец вертикальной линии
    count = 0
    triangle_points = [
        sd.get_point(350, 380),
        sd.get_point(850, 380),
        sd.get_point(600, 550)
    ]
    print(type(triangle_points))
    sd.square(sd.get_point(400, 0), 400, sd.COLOR_ORANGE, width=0)
    sd.square(sd.get_point(400, 0), 400, (100, 100, 100), width=5)

    for y in range(0, 400, 50):
        # левый край экрана
        point = sd.Point(400, y)
        # правый край экрана
        endpoint = sd.Point(800, y)
        # рисуем горизонтальную линию
        sd.line(point, endpoint, color=(100, 100, 100), width=5)
        count += 1
        for x in range(400, 800, 100):
            # условие четности операции рисования линий относительно горизонтальной линии
            if count % 2 == 0:
                # если делится без остатка (кратно 2, чётное), то вертикальная линия без сдвигов
                point = sd.Point(x, y)
                endpoint = sd.Point(x, y + 50)
                sd.line(point, endpoint, color=(100, 100, 100), width=5)
            else:
                # если делится с остатком (нечётное), то сдвигаем начало и конец каждой линии на 50 по горизонтали (х)
                point = sd.Point(x + 50, y)
                endpoint = sd.Point(x + 50, y + 50)
                sd.line(point, endpoint, color=(100, 100, 100), width=5)
    sd.square(sd.get_point(500, 100), 200, sd.COLOR_DARK_YELLOW, width=0)
    sd.square(sd.get_point(500, 100), 200, (100, 100, 100), width=5)
    sd.polygon(triangle_points, sd.COLOR_DARK_RED, 0)



