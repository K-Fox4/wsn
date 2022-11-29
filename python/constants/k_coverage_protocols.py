import config as cf
import math

from python.k_coverage import *

tessellation_protocol_label_map = {
    "square": r'$\it{k}$-CSqu',
    "triangle": r'$DIRACC_k$',
    "irrhex1": r'$\it{k}$-InDi',
}

tessellation_stochastic_protocol_label_map = {
    "square": r'St-$\it{k}$-CSqu',
    "triangle": r'$SCP_k$',
    "irrhex1": r'St-$\it{k}$-InDi',
}

tessellation_protocol_map = {
    "square": 'k-CSqu',
    "triangle": 'DIRACCk',
    "irrhex1": 'k-InDi',
}

tessellation_stochastic_protocol_map = {
    "square": 'k-CSqu',
    "triangle": 'DIRACCk',
    "irrhex1": 'k-InDi',
}

# tessellation_class_map = {
#     "square": Square(
#         sensing_radius=int(cf.COVERAGE_RADIUS),
#         area_length=int(cf.AREA_LENGTH)
#     ),
#     "triangle": ReuleauxTriangle(
#         sensing_radius=int(cf.COVERAGE_RADIUS),
#         area_length=int(cf.AREA_LENGTH)
#     ),
#     "irrhex1": IrregularHexagon1(
#         sensing_radius=int(cf.COVERAGE_RADIUS),
#         area_length=int(cf.AREA_LENGTH)
#     ),
# }


def calculate_stochastic_rs_min(k, alpha, beta, pth):
    return math.pow((-1*math.log(1-math.pow(1-pth, 1/k)))/beta, 1/alpha)


def get_tessellation_class_for_tile(k_coverage_approach: tuple):
    tile_name = k_coverage_approach[0]
    stochastic_sensing = k_coverage_approach[2]

    if tile_name == "square":
        if stochastic_sensing:
            min_stochastic_radius = calculate_stochastic_rs_min(k_coverage_approach[1],
                                                                k_coverage_approach[3],
                                                                k_coverage_approach[4],
                                                                k_coverage_approach[5])
            return Square(sensing_radius=int(min_stochastic_radius),
                          area_length=int(cf.AREA_LENGTH))

        else:
            return Square(sensing_radius=int(cf.COVERAGE_RADIUS),
                          area_length=int(cf.AREA_LENGTH))

    elif tile_name == "triangle":
        if stochastic_sensing:
            min_stochastic_radius = calculate_stochastic_rs_min(k_coverage_approach[1],
                                                                k_coverage_approach[3],
                                                                k_coverage_approach[4],
                                                                k_coverage_approach[5])
            return ReuleauxTriangle(sensing_radius=int(min_stochastic_radius),
                                    area_length=int(cf.AREA_LENGTH))

        else:
            return ReuleauxTriangle(sensing_radius=int(cf.COVERAGE_RADIUS),
                                    area_length=int(cf.AREA_LENGTH))

    elif tile_name == "irrhex1":
        if stochastic_sensing:
            pass
        else:
            return IrregularHexagon1(sensing_radius=int(cf.COVERAGE_RADIUS),
                                     area_length=int(cf.AREA_LENGTH))

