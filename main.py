from cosc262 import *



points = [
    # original
    Vec(0, 8), Vec(-1, 9), Vec(1, 9), Vec(-1, 7), Vec(1, 7),
    Vec(-3, 6), Vec(3, 6), Vec(-4, 4), Vec(4, 4),
    Vec(0, 5), Vec(0, 3), Vec(-1, 3), Vec(1, 3),
    Vec(-2, 2), Vec(2, 2),
    Vec(-2, 0), Vec(2, 0), Vec(-3, -2), Vec(3, -2),
    Vec(-4, -4), Vec(4, -4),

    # shifted down by 0.3
    Vec(0, 7.7), Vec(-1, 8.7), Vec(1, 8.7), Vec(-1, 6.7), Vec(1, 6.7),
    Vec(-3, 5.7), Vec(3, 5.7), Vec(-4, 3.7), Vec(4, 3.7),
    Vec(0, 4.7), Vec(0, 2.7), Vec(-1, 2.7), Vec(1, 2.7),
    Vec(-2, 1.7), Vec(2, 1.7),
    Vec(-2, -0.3), Vec(2, -0.3), Vec(-3, -2.3), Vec(3, -2.3),
    Vec(-4, -4.3), Vec(4, -4.3),
]
print(graham_scan(points))