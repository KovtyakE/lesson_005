# utf8
import simple_draw as sd

def sun_paint():
    start_point = sd.get_point(850, 650)
    sd.circle(start_point, 60, sd.COLOR_YELLOW, 0)
    angle = 0
    for vector in range(10):
        sd.vector(start_point, angle, 200, sd.COLOR_YELLOW, 10)
        angle += 36