import numpy as np
from math import pi
"""TODO: написать логику вычислений"""


def lab_gkh(x, o, b1, t, d, m, b2, e):
    A = (((o - x) * b1) / 1_000_000)
    B = A * 1013.25 * 273 / ((1013.25 + d) * (273 + t))
    RA = (B * 44 / (22.4 * e * m * (b2 / 100))) * 10
    return RA


def lab_titr(x, o, m, e):
    RA = 2.2 * ((x - o) / (e * m))
    return RA


def field_co2(x, o, h, d, t, e):
    A = 0.001 * h * ((pi * d**2) / 4) * (o - x) / (0.0821 * (273 + t))
    B = A / e
    C = B * 12 * 60 / 10**-6
    RA = 10**4 * C / ((pi * d**2) / 4)
    return RA


def field_gkh(x, o, h, l1, l2, t, e):
    A = 10**-3 * h * l1 * l2 * (o - x) / (0.0821 * (273 + t))
    B = A / e
    C = B * 12 * 60 / 10**6
    RA = 10**4 * C / (l1 * l2)
    return RA


def convert_from_gr_to_m2(co2_p_gr):
    pass
