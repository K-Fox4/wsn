import config as cf
import numpy as np
import math

from shapely.geometry import Point, Polygon


class Tessellation:

    def __init__(self):
        self.tiles = []
        self.points = []
        self.x_max = int(cf.AREA_LENGTH)
        self.y_max = int(cf.AREA_WIDTH)


class ReuleauxTriangle(Tessellation):

    def __init__(self):
        super().__init__()

        self.points = self.get_all_points()
        self.tiles = self.get_tiles_info()
        self.total_num_of_tiles = len(self.tiles)

    def get_all_points(self):
        points = []

        extra = 0
        y = 0
        y_ext = round(0.5 * math.sqrt(3) * int(cf.COVERAGE_RADIUS), 2)
        x_ext = int(cf.COVERAGE_RADIUS)
        n = self.x_max // x_ext
        y_iterations = 1 + math.ceil(self.y_max / y_ext)

        for ind_i in range(y_iterations):

            row = []
            x_iterations = n + 1 + extra
            x = 0

            for ind_j in range(x_iterations):

                row.append((x, y))
                # If the row is equally divided by the
                # Reuleaux triangle base
                if not extra:
                    x += x_ext

                # If the row has starting and ending half
                # base divisions
                else:
                    if ind_j == 0 or ind_j == (x_iterations - 2):
                        x += (0.5 * x_ext)
                    else:
                        x += x_ext

            # Add the points for this row
            # to the collection of all
            # points
            points.append(row)

            # Alternate value of var extra
            # consequently
            extra = 0 if extra else 1

            # Increment y
            y += y_ext
            y = round(y, 2)

        return points

    def get_tiles_info(self):
        tiles = []
        x_iterations = len(self.points[0])

        for ind_i in range(len(self.points) - 1):

            for ind_j in range(x_iterations):

                # If the row is equally divided by the
                # Reuleaux triangle base
                if ind_i % 2 == 0:
                    if ind_j == x_iterations - 1:
                        tiles.append(Polygon(
                            [self.points[ind_i][ind_j],
                             self.points[ind_i + 1][ind_j + 1],
                             self.points[ind_i + 1][ind_j]]
                        ))
                    else:
                        tiles.append(Polygon(
                            [self.points[ind_i][ind_j],
                             self.points[ind_i + 1][ind_j + 1],
                             self.points[ind_i + 1][ind_j]]
                        ))
                        tiles.append(Polygon(
                            [self.points[ind_i][ind_j],
                             self.points[ind_i][ind_j + 1],
                             self.points[ind_i + 1][ind_j + 1]]
                        ))

                # If the row has starting and ending half
                # base divisions
                else:
                    if ind_j == 0:
                        tiles.append(Polygon(
                            [self.points[ind_i][ind_j],
                             self.points[ind_i][ind_j + 1],
                             self.points[ind_i + 1][ind_j]]
                        ))
                    else:
                        tiles.append(Polygon(
                            [self.points[ind_i][ind_j],
                             self.points[ind_i + 1][ind_j],
                             self.points[ind_i + 1][ind_j - 1]]
                        ))
                        tiles.append(Polygon(
                            [self.points[ind_i][ind_j],
                             self.points[ind_i][ind_j + 1],
                             self.points[ind_i + 1][ind_j]]
                        ))

        return tiles


class Square(Tessellation):

    def __init__(self):
        super().__init__()

        self.tiles = self.get_tiles_info()
        self.total_num_of_tiles = len(self.tiles)

    def get_tiles_info(self):
        tiles = []
        radius = int(cf.COVERAGE_RADIUS)

        for y in range(0, self.y_max, radius):
            for x in range(0, self.x_max, radius):
                tiles.append(Polygon(
                    [(x, y),
                     (x + radius, y),
                     (x + radius, y + radius),
                     (x, y + radius)]
                ))

        return tiles


class IrregularHexagon1(Tessellation):

    def __init__(self, factor=5):
        super().__init__()

        self.factor = factor
        self.points = self.get_all_points()
        self.tiles = self.get_tiles_info()
        self.total_num_of_tiles = len(self.tiles)

    def get_all_points(self):
        points = []

        side = int(cf.COVERAGE_RADIUS) / self.factor
        x_ext_1 = (2 * self.factor - 1) * side
        x_ext_2 = int(cf.COVERAGE_RADIUS)
        x_iterations = 2 * math.ceil(self.x_max / (x_ext_1 + x_ext_2))

        y = 0
        y_ext = round((self.factor - 1) * 0.5 * math.sqrt(3) * side, 2)
        y_iterations = 1 + math.ceil(self.y_max / y_ext)

        for ind_i in range(y_iterations):

            row = []
            x = 0 if ind_i % 2 == 0 else (self.factor - 1) * 0.5 * side

            for ind_j in range(x_iterations):

                row.append((x, y))

                # If the starting hexagon has a x
                # coordinate as zero
                if ind_i % 2 == 0:

                    # Odd position x extension
                    if ind_j % 2 == 0:
                        x += x_ext_1

                    # Even position x extension
                    else:
                        x += x_ext_2

                # If the starting hexagon has a
                # non-zero x coordinate
                else:

                    # Odd position x extension
                    if ind_j % 2 == 0:
                        x += x_ext_2

                    # Even position x extension
                    else:
                        x += x_ext_1

            # Add the points for this row
            # to the collection of all
            # points
            points.append(row)

            # Increment y
            y += y_ext
            y = round(y, 2)

        return points

    def get_tiles_info(self):
        tiles = []
        x_iterations = len(self.points[0]) - 1
        y_iterations = len(self.points)

        for ind_i in range(0, y_iterations, 2):

            for ind_j in range(x_iterations):

                # Combination of half and full
                # Irregular hexagonal tiles
                if ind_i == 0:

                    # Half Irregular Hexagonal tile
                    if ind_j % 2 == 0:
                        tiles.append(Polygon(
                            [self.points[ind_i][ind_j],
                             self.points[ind_i + 1][ind_j],
                             self.points[ind_i + 1][ind_j + 1],
                             self.points[ind_i][ind_j + 1]]
                        ))

                    # Full Irregular Hexagonal tile
                    else:
                        tiles.append(Polygon(
                            [self.points[ind_i][ind_j],
                             self.points[ind_i + 1][ind_j],
                             self.points[ind_i + 1][ind_j + 1],
                             self.points[ind_i + 1][ind_j + 2],
                             self.points[ind_i][ind_j + 2],
                             self.points[ind_i][ind_j + 1]]
                        ))

                # Uniform gap between the consecutive
                # Irregular hexagonal tiles
                elif ind_i == y_iterations - 1:

                    # Generating tile with uniform gaps
                    if ind_j % 2 == 0:
                        tiles.append(Polygon(
                            [self.points[ind_i][ind_j],
                             self.points[ind_i - 1][ind_j],
                             self.points[ind_i - 1][ind_j + 1],
                             self.points[ind_i][ind_j + 1],
                             self.points[ind_i + 1][ind_j + 1],
                             self.points[ind_i + 1][ind_j]]
                        ))

                # Continuous Irregular Hexagonal tiles
                else:

                    # Selecting Irregular Hexagon using
                    # middle left vertex
                    if ind_j % 2 == 0:
                        tiles.append(Polygon(
                            [self.points[ind_i][ind_j],
                             self.points[ind_i - 1][ind_j],
                             self.points[ind_i - 1][ind_j + 1],
                             self.points[ind_i][ind_j + 1],
                             self.points[ind_i + 1][ind_j + 1],
                             self.points[ind_i + 1][ind_j]]
                        ))

                    # Selecting Irregular Hexagon using
                    # bottom left vertex
                    else:
                        tiles.append(Polygon(
                            [self.points[ind_i][ind_j],
                             self.points[ind_i + 1][ind_j],
                             self.points[ind_i + 1][ind_j + 1],
                             self.points[ind_i + 1][ind_j + 2],
                             self.points[ind_i][ind_j + 2],
                             self.points[ind_i][ind_j + 1]]
                        ))

        return tiles


if __name__ == "__main__":

    """
    Testing of Reuleaux Triangle tessellation code
    """
    # test = ReuleauxTriangle()
    #
    # print("Calculated points for the Reuleaux triangle tessellation are,\n")
    # print(*test.points, sep="\n")
    #
    # print(f"\nTotal tiles generated for this tessellation are {len(test.tiles)}")

    """
        Testing of Square tessellation code
    """
    # test = Square()

    """
        Testing of Irregular Hexagon (Type 1 of Kalyan) tessellation code
    """
    test = IrregularHexagon1(factor=5)

    print("Calculated points for the Reuleaux triangle tessellation are,\n")
    print(*test.points, sep="\n")

    # print(f"\nTotal tiles generated for this tessellation are {len(test.tiles)}")

    points = [(np.random.uniform(0, cf.AREA_WIDTH), np.random.uniform(0, cf.AREA_LENGTH)) for _ in range(1000)]
    k = 3
    k_coverage_nodes = []

    for tile in test.tiles:
        curr_degree_of_cov = 0
        for point in points:
            if tile.contains(Point(point[0], point[1])):
                k_coverage_nodes.append(point)
                curr_degree_of_cov += 1

            if curr_degree_of_cov == k:
                break

    print(f"Total number of tile are {test.total_num_of_tiles}")
    print(f"Total locations selected for all the tiles are {len(k_coverage_nodes)}")
