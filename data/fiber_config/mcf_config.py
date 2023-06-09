
MCF_2 = {
    "adjs": {
        0: (1),
        1: (0)
    }
}

MCF_7 = {
    "adjs": {
        0: (1, 2, 3, 4, 5, 6),
        1: (6, 2, 0),
        2: (1, 0, 3),
        3: (2, 0, 4),
        4: (3, 0, 5), 
        5: (4, 0, 6),
        6: (5, 0, 1),
    }, 
    "rings": 1,
    "core_per_ring": (6),
    "central_node": True
}

MCF_12 = {
    "adjs": {
        0: (1, 11),
        1: (0, 2),
        2: (1, 3),
        3: (2, 4),
        4: (3, 5),
        5: (4, 6),
        6: (5, 7),
        7: (6, 8),
        8: (7, 9),
        9: (8, 10),
        10: (9, 11),
        11: (10, 0)
    }, 
    "rings": 1,
    "core_per_ring": (12),
    "central_node": False
}

MCF_19 = {
    "adjs": {
        0: (1, 2, 3, 4, 5, 6),
        1: (2, 0, 6, 7, 8, 9),
        2: (3, 0, 1, 9, 10, 11),
        3: (4, 0, 2, 11, 12, 13),
        4: (15, 5, 0, 3, 13, 14),
        5: (16, 17, 6, 0, 4, 15),
        6: (17, 18, 7, 1, 0, 5),
        7: (8, 1, 6, 18),
        8: (9, 1, 7),
        9: (10, 2, 1, 8),
        10: (11, 2, 9),
        11: (12, 3, 2, 10),
        12: (13, 3, 11),
        13: (14, 4, 3, 12),
        14: (15, 4, 13),
        15: (16, 5, 4, 14),
        16: (17, 5, 15),
        17: (18, 6, 5, 16),
        18: (17, 6, 7)
    }, 
    "rings": 2,
    "core_per_ring": (12, 6),
    "central_node": True
}

MCF_22 = {
    "adjs": {
        0: (1, 2, 3, 4, 5, 6, 7),
        1: (2, 0, 7, 19, 20, 21, 8),
        2: (3, 0, 1, 21, 8, 9, 10),
        3: (4, 0, 2, 9, 10, 11, 12),
        4: (0, 3, 11, 12, 13, 14, 5),
        5: (0, 4, 13, 14, 15, 16, 6),
        6: (0, 5, 15, 16, 17, 18, 7),
        7: (0, 6, 17, 18, 19, 20, 1),
        8: (9, 2, 1, 21),
        9: (10, 3, 2, 8),
        10: (11, 3, 2, 9),
        11: (12, 4, 3, 10),
        12: (13, 4, 3, 11),
        13: (14, 5, 4, 12),
        14: (15, 5, 4, 13),
        15: (16, 6, 5, 14),
        16: (17, 6, 5, 15),
        17: (18, 7, 6, 16),
        18: (19, 7, 6, 17),
        19: (20, 1, 7, 18),
        20: (21, 1, 7, 19),
        21: (8, 2, 1, 20)
    },
    "rings": 2,
    "core_per_ring": (14, 7),
    "central_node": True,
}

MCF_30 = {
    "adjs": {
        0: (1, 5, 16, 17, 6),
        1: (2, 0, 6, 7, 8),
        2: (3, 1, 8, 9, 10),
        3: (4, 2, 10, 11, 12),
        4: (5, 3, 12, 13, 14),
        5: (4, 14, 15, 16, 0),
        6: (0, 1, 7, 19, 18, 17),
        7: (20, 8, 1, 6, 19),
        8: (20, 21, 9, 2, 1, 7),
        9: (22, 10, 2, 8, 21),
        10: (23, 11, 3, 2, 8, 21),
        11: (24, 12, 3, 10, 23),
        12: (25, 13, 4, 3, 11, 24),
        13: (26, 14, 4, 12, 25),
        14: (13, 26, 27, 15, 5, 4),
        15: (28, 16, 5, 14, 27),
        16: (5, 15, 28, 29, 17, 0),
        17: (18, 6, 0, 16, 29),
        18: (17, 19, 6),
        19: (18, 6, 7),
        20: (7, 8, 21),
        21: (9, 8, 20),
        22: (23, 10, 9),
        23: (11, 10, 22),
        24: (25, 12, 11),
        25: (13, 12, 24),
        26: (27, 14, 13),
        27: (15, 14, 26),
        28: (15, 16, 29),
        29: (28, 16, 17)
    },
    "rings": 3,
    "core_per_ring": (12, 12, 6),
    "central_node": False
}