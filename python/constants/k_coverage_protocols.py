import config as cf

from python.k_coverage import *

tessellation_protocol_label_map = {
    "square": r'$\it{k}$-CSqu',
    "triangle": r'$DIRACC_k$',
    "irrhex1": r'$\it{k}$-InDi',
}

tessellation_protocol_map = {
    "square": 'k-CSqu',
    "triangle": 'DIRACCk',
    "irrhex1": 'k-InDi',
}

tessellation_class_map = {
    "square": Square(
        sensing_radius=int(cf.COVERAGE_RADIUS),
        area_length=int(cf.AREA_LENGTH)
    ),
    "triangle": ReuleauxTriangle(
        sensing_radius=int(cf.COVERAGE_RADIUS),
        area_length=int(cf.AREA_LENGTH)
    ),
    "irrhex1": IrregularHexagon1(
        sensing_radius=int(cf.COVERAGE_RADIUS),
        area_length=int(cf.AREA_LENGTH)
    ),
}
