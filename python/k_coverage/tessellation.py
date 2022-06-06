import config as cf
import numpy as np
import math

from shapely.geometry import Point, Polygon


class Tile(Polygon):

    def __init__(self, shell=None, tile_name=None, side=None, holes=None):

        Polygon.__init__(self, shell, holes)
        self.tile_name = tile_name
        self.side = side
        self.inner_radius = self.calculate_inner_radius()

    def calculate_inner_radius(self):
        result = None
        if self.tile_name == "irrhex1":
            result = round(0.5 * math.sqrt(3) * self.side, 2)
        elif self.tile_name == "square":
            result = round(0.5 * math.sqrt(2 - math.sqrt(3)) * self.side, 2)
        elif self.tile_name == "triangle":
            result = round(0.5 * (2 - math.sqrt(3)) * self.side, 2)

        return result

    def distance_from_centroid(self, x, y):
        centroid = self.centroid
        return round(math.sqrt(
            math.pow(centroid.x - x, 2) + math.pow(centroid.y - y, 2)),
            2)

    def move_instructions(self, x, y):
        centroid = self.centroid
        d = self.distance_from_centroid(x, y)

        cos_theta = abs(centroid.x - x) / d
        sin_theta = abs(centroid.y - y) / d

        # Per round, sensor speed is the distance
        # moved by a sensor
        x_new = (d - cf.SENSOR_SPEED) * cos_theta
        y_new = (d - cf.SENSOR_SPEED) * sin_theta

        distance_to_move = cf.SENSOR_SPEED

        return x_new, y_new, distance_to_move


class Tessellation:

    def __init__(self):
        self.tile_name = None
        self.tiles = []
        self.points = []
        self.x_max = int(cf.AREA_LENGTH)
        self.y_max = int(cf.AREA_WIDTH)


class ReuleauxTriangle(Tessellation):

    def __init__(self):
        super().__init__()

        self.tile_name = "triangle"
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
        x_iterations = len(self.points[0]) - 1

        for ind_i in range(len(self.points) - 1):

            for ind_j in range(x_iterations):

                # If the row is equally divided by the
                # Reuleaux triangle base
                if ind_i % 2 == 0:

                    """
                    Old code
                    """

                    """if ind_j == x_iterations - 1:
                        tiles.append(Tile(
                            [self.points[ind_i][ind_j],
                             self.points[ind_i + 1][ind_j + 1],
                             self.points[ind_i + 1][ind_j]],
                            self.tile_name,
                            int(cf.COVERAGE_RADIUS)
                        ))
                    else:
                        tiles.append(Tile(
                            [self.points[ind_i][ind_j],
                             self.points[ind_i + 1][ind_j + 1],
                             self.points[ind_i + 1][ind_j]],
                            self.tile_name,
                            int(cf.COVERAGE_RADIUS)
                        ))
                        tiles.append(Tile(
                            [self.points[ind_i][ind_j],
                             self.points[ind_i][ind_j + 1],
                             self.points[ind_i + 1][ind_j + 1]],
                            self.tile_name,
                            int(cf.COVERAGE_RADIUS)
                        ))"""

                    if ind_j == 0:
                        tiles.append(Tile(
                            [self.points[ind_i][ind_j],
                             self.points[ind_i][ind_j + 1],
                             self.points[ind_i + 1][ind_j + 1]],
                            self.tile_name,
                            int(cf.COVERAGE_RADIUS)
                        ))

                    else:
                        tiles.append(Tile(
                            [self.points[ind_i][ind_j],
                             self.points[ind_i - 1][ind_j + 1],
                             self.points[ind_i][ind_j + 1],
                             self.points[ind_i + 1][ind_j + 1]],
                            self.tile_name,
                            int(cf.COVERAGE_RADIUS)
                        ))

                # If the row has starting and ending half
                # base divisions
                else:

                    """
                    Old code
                    """

                    """if ind_j == 0:
                        tiles.append(Tile(
                            [self.points[ind_i][ind_j],
                             self.points[ind_i][ind_j + 1],
                             self.points[ind_i + 1][ind_j]],
                            self.tile_name,
                            int(cf.COVERAGE_RADIUS)
                        ))
                    else:
                        tiles.append(Tile(
                            [self.points[ind_i][ind_j],
                             self.points[ind_i + 1][ind_j],
                             self.points[ind_i + 1][ind_j - 1]],
                            self.tile_name,
                            int(cf.COVERAGE_RADIUS)
                        ))
                        tiles.append(Tile(
                            [self.points[ind_i][ind_j],
                             self.points[ind_i][ind_j + 1],
                             self.points[ind_i + 1][ind_j]],
                            self.tile_name,
                            int(cf.COVERAGE_RADIUS)
                        ))"""

                    index = ind_j + 1

                    if index == 1:
                        tiles.append(Tile(
                            [self.points[ind_i][ind_j],
                             self.points[ind_i + 1][ind_j - 1],
                             self.points[ind_i - 1][ind_j - 1]],
                            self.tile_name,
                            int(cf.COVERAGE_RADIUS)
                        ))
                        tiles.append(Tile(
                            [self.points[ind_i][ind_j],
                             self.points[ind_i - 1][ind_j + 1],
                             self.points[ind_i][ind_j + 1],
                             self.points[ind_i + 1][ind_j]],
                            self.tile_name,
                            int(cf.COVERAGE_RADIUS)
                        ))

                    elif ind_j == x_iterations - 1:
                        tiles.append(Tile(
                            [self.points[ind_i][ind_j],
                             self.points[ind_i - 1][ind_j + 1],
                             self.points[ind_i + 1][ind_j + 1]],
                            self.tile_name,
                            int(cf.COVERAGE_RADIUS)
                        ))

                    else:
                        tiles.append(Tile(
                            [self.points[ind_i][ind_j],
                             self.points[ind_i - 1][ind_j + 1],
                             self.points[ind_i][ind_j + 1],
                             self.points[ind_i + 1][ind_j]],
                            self.tile_name,
                            int(cf.COVERAGE_RADIUS)
                        ))

        return tiles


class Square(Tessellation):

    def __init__(self):
        super().__init__()

        self.tile_name = "square"
        self.tiles = self.get_tiles_info()
        self.total_num_of_tiles = len(self.tiles)

    def get_tiles_info(self):
        tiles = []
        radius = int(cf.COVERAGE_RADIUS)

        for y in range(0, self.y_max, radius):
            for x in range(0, self.x_max, radius):
                tiles.append(Tile(
                    [(x, y),
                     (x + radius, y),
                     (x + radius, y + radius),
                     (x, y + radius)],
                    self.tile_name,
                    int(cf.COVERAGE_RADIUS)
                ))

        return tiles


class IrregularHexagon1(Tessellation):

    def __init__(self, factor=5):
        super().__init__()

        self.tile_name = "irrhex1"
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
                        tiles.append(Tile(
                            [self.points[ind_i][ind_j],
                             self.points[ind_i + 1][ind_j],
                             self.points[ind_i + 1][ind_j + 1],
                             self.points[ind_i][ind_j + 1]],
                            self.tile_name,
                            int(cf.COVERAGE_RADIUS) // self.factor
                        ))

                    # Full Irregular Hexagonal tile
                    else:
                        tiles.append(Tile(
                            [self.points[ind_i][ind_j],
                             self.points[ind_i + 1][ind_j],
                             self.points[ind_i + 1][ind_j + 1],
                             self.points[ind_i + 1][ind_j + 2],
                             self.points[ind_i][ind_j + 2],
                             self.points[ind_i][ind_j + 1]],
                            self.tile_name,
                            int(cf.COVERAGE_RADIUS) // self.factor
                        ))

                # Uniform gap between the consecutive
                # Irregular hexagonal tiles
                elif ind_i == y_iterations - 1:

                    # Generating tile with uniform gaps
                    if ind_j % 2 == 0:
                        tiles.append(Tile(
                            [self.points[ind_i][ind_j],
                             self.points[ind_i - 1][ind_j],
                             self.points[ind_i - 1][ind_j + 1],
                             self.points[ind_i][ind_j + 1],
                             self.points[ind_i + 1][ind_j + 1],
                             self.points[ind_i + 1][ind_j]],
                            self.tile_name,
                            int(cf.COVERAGE_RADIUS) // self.factor
                        ))

                # Continuous Irregular Hexagonal tiles
                else:

                    # Selecting Irregular Hexagon using
                    # middle left vertex
                    if ind_j % 2 == 0:
                        tiles.append(Tile(
                            [self.points[ind_i][ind_j],
                             self.points[ind_i - 1][ind_j],
                             self.points[ind_i - 1][ind_j + 1],
                             self.points[ind_i][ind_j + 1],
                             self.points[ind_i + 1][ind_j + 1],
                             self.points[ind_i + 1][ind_j]],
                            self.tile_name,
                            int(cf.COVERAGE_RADIUS) // self.factor
                        ))

                    # Selecting Irregular Hexagon using
                    # bottom left vertex
                    else:
                        tiles.append(Tile(
                            [self.points[ind_i][ind_j],
                             self.points[ind_i + 1][ind_j],
                             self.points[ind_i + 1][ind_j + 1],
                             self.points[ind_i + 1][ind_j + 2],
                             self.points[ind_i][ind_j + 2],
                             self.points[ind_i][ind_j + 1]],
                            self.tile_name,
                            int(cf.COVERAGE_RADIUS) // self.factor
                        ))

        return tiles


if __name__ == "__main__":

    """
    Testing of Reuleaux Triangle tessellation code
    """
    test = ReuleauxTriangle()

    print("Calculated points for the Reuleaux triangle tessellation are,\n")
    print(*test.points, sep="\n")
    #
    # print(f"\nTotal tiles generated for this tessellation are {len(test.tiles)}")

    """
        Testing of Square tessellation code
    """
    # test = Square()

    """
        Testing of Irregular Hexagon (Type 1 of Kalyan) tessellation code
    """
    # test = IrregularHexagon1(factor=5)

    # print("Calculated points for the Irregular Hexagon (Type 1 of Kalyan) tessellation are,\n")
    # print(*test.points, sep="\n")

    for i in range(len(test.tiles)):
        print(f"The Centroid of Tile#{i} is {test.tiles[i].centroid}")

    print(f"\nTotal tiles generated for this tessellation are {len(test.tiles)}")

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
