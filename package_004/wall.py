# -*- coding: utf-8 -*-

import simple_draw as sd


def wall_paint():
    # счетчик для определения сдвига, нужно ли сдвигать начало и конец вертикальной линии
    count = 0
    for y in range(-35, 400, 50):
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
