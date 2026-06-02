import math
from functools import cmp_to_key

from cosc262.computational_geometry.kd_tree import KdTree
from cosc262.computational_geometry.vector import Vec


def lts_points(a,b):
    if a.x < b.x:
        return True
    elif a.x > b.x:
        return False

    if a.y < b.y:
        return True

    return False

def closest_pair(points):
    """
    Uses a line sweep algorithm to find the closest pair in a list of points
    :param points: the points to check
    :return: the closest pair of points to each other in a list of points
    """

    if len(points) < 2:
        raise Exception("Not enough points")

    tree = KdTree(points)
    points = sorted(points, key=cmp_to_key(lambda x,y: lts_points(x,y)))

    pair = points[0], points[1]
    lowest_distance_sq = (points[0] - points[1]).lensq()
    lowest_distance = math.sqrt(lowest_distance_sq)

    for p in points:
        bottom_left = Vec(p.x - lowest_distance, p.y - lowest_distance)
        top_right = Vec(p.x, p.y + lowest_distance)

        for q in tree.points_in_range(bottom_left, top_right):
            if p == q:
                continue

            distance_sq = (p-q).lensq()

            if distance_sq < lowest_distance_sq:
                lowest_distance_sq = distance_sq
                lowest_distance = math.sqrt(lowest_distance_sq)
                pair = p, q


    return pair