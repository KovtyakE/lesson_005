# -*- coding: utf-8 -*-
from random import randint
import simple_draw as sd


def tree_paint():
    first_point = sd.get_point(1150, 150)

    def draw_branches(start_point, start_angle, start_length, width):
        # two branches, left and right
        branch_1 = sd.get_vector(start_point=start_point, angle=start_angle + 30, length=start_length, width=width)
        branch_1.draw(sd.random_color())
        branch_2 = sd.get_vector(start_point=start_point, angle=start_angle - 30, length=start_length, width=width)
        branch_2.draw(sd.random_color())
        # target 2, after first two branches changing length, angle, width and start point of drawing
        start_length *= (0.75 + (randint(-10, 10) / 100))
        start_point = branch_1.end_point
        start_angle = branch_1.angle + randint(-12, 12)
        width = width - 1
        if start_length > 10:
            # continuing of left root, recursion
            draw_branches(start_point=start_point, start_angle=start_angle, start_length=start_length, width=width)
        start_point = branch_2.end_point
        rand_int = randint(-12, 12)
        start_angle = branch_2.angle - rand_int
        if start_length > 10:
            # continuing of right root, recursion
            draw_branches(start_point=start_point, start_angle=start_angle, start_length=start_length, width=width)

    # first line, vertical part of tree
    sd.line(sd.get_point(1150, 0), sd.get_point(1150, 150), width=14)
    draw_branches(start_point=first_point, start_angle=90, start_length=105, width=12)
