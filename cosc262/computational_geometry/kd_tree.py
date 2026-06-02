from cosc262.computational_geometry.vector import Vec


class KdTree:
    """
    A sorting of 2d data that allows for efficient repeated range searches, lookups and closest neighbors.
    """
    def __init__(self, points, max_points=2, depth=0, max_depth=100):
        """
        Creates a Kd-Tree based on the given points
        :param points: the points being ordered
        :param max_points: the maximum points in a leaf node
        :param depth: the current depth (default zero)
        :param max_depth: the maximum recursion depth
        """
        self.depth = depth
        if len(points) <= max_points or depth > max_depth:
            self.leaf = True
            self.points = points
        else:
            self.leaf = False
            self.axis = depth % 2
            points.sort(key=lambda x: x[self.axis])
            mid = len(points) // 2
            self.coord = points[mid-1][self.axis]
            self.left_tree = KdTree(points[:mid], max_points, depth+1, max_depth)
            self.right_tree = KdTree(points[mid:], max_points, depth+1, max_depth)

    def is_leaf(self):
        """
        Returns true if the node is a leaf node
        :return: true if the node is a leaf node
        """
        return self.leaf

    def __repr__(self):
        indent = "     "
        if not self.is_leaf():
            return f"{indent * self.depth}KdTree({self.coord}, {self.axis})\n" + \
                    repr(self.left_tree) + "\n" + \
                    repr(self.right_tree)
        else:
            return indent * self.depth + repr(self.points)

    def contains(self, point):
        """
        Returns true if the Kd-Tree contains the given point
        :param point: a point
        :return: true if the Kd-Tree contains the given point
        """
        return point in self.get_leaf(point)

    def __contains__(self, item):
        return self.contains(item)

    def points_in_range(self, bottom_left, top_right):
        """
        Returns a list of the points in the range given
        :param bottom_left: a point representing the bottom left of the range (inclusive)
        :param top_right: a point representing the top right of the range (inclusive)
        :return: a list of the points in the range given
        """
        if self.is_leaf():
            return [
                p for p in self.points
                if bottom_left.x <= p.x <= top_right.x
                and bottom_left.y <= p.y <= top_right.y
            ]

        result = []

        if bottom_left[self.axis] <= self.coord:
            result += self.left_tree.points_in_range(bottom_left, top_right)

        if top_right[self.axis] >= self.coord:
            result += self.right_tree.points_in_range(bottom_left, top_right)

        return result

    def get_leaf(self, point):
        """
        Returns a list of points in the same leaf as the point
        :param point: a point
        :return: list of points in the same leaf as the point
        """
        if self.is_leaf():
            return self.points
        else:
            if point[self.axis] > self.coord:
                return self.right_tree.get_leaf(point)

            return self.left_tree.get_leaf(point)

def closest_neighbor(tree, point):
    """
    Finds the closest point in the KdTree to the given point p
    :param tree: a KdTree with points
    :param point: a point p
    :return: the closest point in the KdTree to the given point p
    """
    leaf_points = tree.get_leaf(point)
    closest_leaf_point = min(leaf_points, key=lambda x: (x - point).lensq())
    d = (closest_leaf_point - point).lensq()

    points = tree.points_in_range(Vec(point.x - d, point.y - d), Vec(point.x + d, point.y + d))
    closest_point = min(points, key=lambda x: (x - point).lensq())
    return closest_point