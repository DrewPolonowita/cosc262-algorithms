def signed_area(a, b, c):
    """
    Returns twice the area of a triangle formed by the points
    :return: twice the area of a triangle formed by the points
    """
    p = b - a
    q = c - a

    return p.x * q.y - q.x * p.y


def on_line_segment(p, a, b):
    """
    Returns true if p is on the line segment formed by a and b
    :param p: a point p
    :param a: a point a
    :param b: a point b
    :return: true if p is on the line segment formed by a and b
    """
    return signed_area(p, a, b) == 0

def is_ccw(a, b, c):
    """
    Returns true if c is left of b from the perspective of a
    :param a: anchor point a
    :param b: a point b
    :param c: a point c
    :return: true if c is left of b from the anchor a
    """
    return signed_area(a, b, c) > 0

def do_lines_intersect(a, b, c, d):
    """
    Returns true if the line segment formed from a to b intersects with the line segment
    formed from c to d
    :param a: a point a
    :param b: a point b
    :param c: a point c
    :param d: a point d
    :return: true if the line segment formed from a to b intersects with the line segment formed from c to d
    """

    line_ab_intersects = not (is_ccw(a, d, b) == is_ccw(a, c, b))
    line_cd_intersects = not (is_ccw(c, a, d) == is_ccw(c, b, d))
    return line_ab_intersects and line_cd_intersects