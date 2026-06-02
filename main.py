from cosc262 import *

points = [
    Vec(-4, -4),  # SW
    Vec(-4,  4),  # NW
    Vec( 4,  4),  # NE
    Vec( 4, -4),  # SE
    Vec(-2, -1),  # SW inner
    Vec( 2, -1),  # SE inner
    Vec(-2,  1),  # NW inner
    Vec( 2,  1)   # NE inner
]

bottom_left = Vec(-3, -3)
top_right   = Vec( 3,  0)


tree = QuadTree(points, Vec(-1, 2), 5)

print(tree.points_in_range(bottom_left, top_right))