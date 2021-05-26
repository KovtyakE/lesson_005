# -*- coding: utf-8 -*-

import simple_draw as sd


def rainbow_paint():
    rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                      sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)
    point = sd.Point(130, -350)
    radius = 1750
    for color in rainbow_colors:
        radius -= 30
        sd.circle(point, radius, color, 30)
