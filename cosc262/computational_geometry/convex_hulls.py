from functools import cmp_to_key

from cosc262.computational_geometry.helper_methods import is_ccw, signed_area


def gift_wrap(points):
    """
    Uses the gift wrap algorithm to create a convex hull around a set of points
    :param points: a set of points
    :return: a convex hull for this set of points
    """
    min_point = get_min_point(points)
    convex_hull = [min_point]

    while len(convex_hull) == 1 or not convex_hull[0] == convex_hull[-1]:

        candidate = None

        for p in points:
            if not p == convex_hull[-1]:
                if candidate is None or not is_ccw(convex_hull[-1], candidate, p):
                    candidate = p

        convex_hull.append(candidate)

    convex_hull.pop()
    return convex_hull


def get_min_point(points):
    min_point = points[0]

    for point in points:
        if point.y < min_point.y:
            min_point = point
        elif point.y == min_point.y:
            if point.x < min_point.x:
                min_point = point

    return min_point


def graham_scan(points):
    """
    Uses the graham scan algorithm to create a convex hull around a set of points
    :param points: a set of points
    :return: a convex hull for this set of points
    """
    min_point = get_min_point(points)
    points = sorted(points, key=cmp_to_key(lambda x,y: signed_area(min_point, y, x)))

    convex_hull = [points[-1], points[0], points[1]]

    for p in points[2:-1]:

        while not is_ccw(convex_hull[-2], convex_hull[-1], p):
            convex_hull.pop()
        convex_hull.append(p)

    return convex_hull