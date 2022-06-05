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
    "square": Square(),
    "triangle": ReuleauxTriangle(),
    "irrhex1": IrregularHexagon1(),
}
