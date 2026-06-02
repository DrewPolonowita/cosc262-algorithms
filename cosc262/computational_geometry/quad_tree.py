from cosc262.computational_geometry.vector import Vec

class QuadTree:
    """
    A sorting of 2d data that allows for efficient repeated range searches and lookups.
    """
    def __init__(self, points, centre, size, max_points=2, depth=0, max_depth=100):
        """
        Creates a quadtree with the points given and the size
        :param points: the points for the tree
        :param centre: the centre of the tree
        :param size: the size of the tree
        :param max_points: the max amount of points in a leaf node
        :param depth: the current depth
        :param max_depth: the maximum recursive depth
        """
        self.depth = depth
        if len(points) <= max_points or depth > max_depth:
            self.leaf = True
            self.points = points
        else:
            self.leaf = False
            self.centre = centre
            self.size = size

            child_centres = [
                Vec(centre.x - size/2, centre.y + size/2),
                Vec(centre.x + size / 2, centre.y + size / 2),
                Vec(centre.x + size / 2, centre.y - size / 2),
                Vec(centre.x - size / 2, centre.y - size / 2)
            ]
            child_size = size / 2
            child_points = [[] for _ in range(4)]

            for point in points:
                if point.x <= centre.x and point.y > centre.y:
                    child_points[0].append(point)
                elif point.x > centre.x and point.y > centre.y:
                    child_points[1].append(point)
                elif point.x > centre.x and point.y <= centre.y:
                    child_points[2].append(point)
                else:
                    child_points[3].append(point)

            self.children = [QuadTree(child_points[i], child_centres[i], child_size, max_points, depth+1, max_depth) for i in range(4)]

    def is_leaf(self):
        """
        Returns true if the node is a leaf node
        :return: true if the node is a leaf node
        """
        return self.leaf

    def __repr__(self):
        indent = "     "
        if not self.is_leaf():
            return f"{indent * self.depth}QuadTree({self.centre}, {self.size})\n" + \
                repr(self.children[0]) + "\n" + \
                repr(self.children[1]) + "\n" + \
                repr(self.children[2]) + "\n" + \
                repr(self.children[3]) + "\n"
        else:
            return indent * self.depth + repr(self.points)

    def contains(self, point):
        """
        Returns true if the point is in the quadtree
        :param point: a point
        :return: true if the point is in the quadtree
        """

        if self.is_leaf():
            return point in self.points
        else:
            if point.x <= self.centre.x and point.y > self.centre.y:
                return point in self.children[0]
            elif point.x > self.centre.x and point.y > self.centre.y:
                return point in self.children[1]
            elif point.x > self.centre.x and point.y <= self.centre.y:
                return point in self.children[2]
            else:
                return point in self.children[3]

    def __contains__(self, point):
        return self.contains(point)

    def points_in_range(self, bottom_left, top_right):
        """
        Returns a list of the points in a range
        :param bottom_left: the bottom left point of the range
        :param top_right: the top right point of the range
        :return: a list of the points in a range
        """
        if self.is_leaf():
            points = []
            for point in self.points:
                if point.x >= bottom_left.x and point.y >= bottom_left.y:
                    if point.x <= top_right.x and point.y <= top_right.y:
                        points.append(point)
            return points


        else:

            points = []
            bottom_in_sw = bottom_left.x <= self.centre.x and bottom_left.y <= self.centre.y
            bottom_in_se = bottom_left.x > self.centre.x and bottom_left.y <= self.centre.y
            bottom_in_ne = bottom_left.x > self.centre.x and bottom_left.y > self.centre.y
            bottom_in_nw = bottom_left.x <= self.centre.x and bottom_left.y > self.centre.y

            top_in_sw = top_right.x <= self.centre.x and top_right.y <= self.centre.y
            top_in_se = top_right.x > self.centre.x and top_right.y <= self.centre.y
            top_in_ne = top_right.x > self.centre.x and top_right.y > self.centre.y
            top_in_nw = top_right.x <= self.centre.x and top_right.y > self.centre.y

            if bottom_in_sw and top_in_ne:
                for child in self.children:
                    points += child.points_in_range(bottom_left, top_right)
            else:
                if bottom_in_sw or top_in_sw:
                    points += self.children[3].points_in_range(bottom_left, top_right)
                if bottom_in_se or top_in_se:
                    points += self.children[2].points_in_range(bottom_left, top_right)
                if bottom_in_ne or top_in_ne:
                    points += self.children[1].points_in_range(bottom_left, top_right)
                if bottom_in_nw or top_in_nw:
                    points += self.children[0].points_in_range(bottom_left, top_right)


            return points