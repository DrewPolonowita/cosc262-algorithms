from .helper_methods import is_ccw, on_line_segment, do_lines_intersect
from .vector import Vec

def in_convex_polygon(p, polygon):
    """
    Returns true if the point p is in the convex polygon
    :param p: a point p
    :param polygon: a convex polygon defined as a list of vertices
    :return: true if the point p is in the convex polygon
    """

    for p0, p1 in zip(polygon, polygon[1:] + [polygon[0]]):
        if not is_ccw(p0, p1, p) and not on_line_segment(p, p0, p1):
            return False

    return True


def in_simple_polygon(p, polygon):
    """
    Returns true if the point p is in the simple polygon
    :param p: a point p
    :param polygon: a simple polygon defined as a list of vertices
    :return: true if the point p is in the simple polygon
    """
    max_x, min_x, max_y, min_y = get_limits_of_points(polygon)

    if p.x > max_x or p.x < min_x:
        return False
    elif p.y > max_y or p.y < min_y:
        return False

    q = Vec(max_x + 1, p.y)
    k = 0

    for p0, p1 in zip(polygon, polygon[1:] + [polygon[0]]):
        if do_lines_intersect(p, q, p0, p1):
            k += 1

    return k % 2 == 1




def get_limits_of_points(points):
    max_x = points[0].x
    min_x = points[0].x
    max_y = points[0].y
    min_y = points[0].y

    for point in points:
        if point.x > max_x:
            max_x = point.x
        if point.x < min_x :
            min_x = point.x

        if point.y > max_y:
            max_y = point.y
        if point.y < min_y:
            min_y = point.y

    return max_x, min_x, max_y, min_y