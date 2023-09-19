from math import pi


def lab_gkh(x, o, b1, t, d, m, b2, e):
    # Function returns value in mgC02g-2h-1
    a = ((o - x) * b1) / 1_000_000
    b = a * d * 273 / (1013.25 * (273 + t))
    ra = (b * 44) / ((22.4 * e) * (m - (b2 / 100)))
    return ra


def lab_titr(x, o, m, e):
    ra = 2.2 * ((x - o) / (e * m))
    return ra


def field_co2(x, o, h, d, t, e):
    A = 0.001 * h * ((pi * d**2) / 4) * (o - x) / (0.0821 * (273 + t))
    B = A / e
    C = B * 12 * 60 / 10**-6
    ra = 10**4 * C / ((pi * d**2) / 4)
    return ra


def field_gkh(x, o, h, l1, l2, t, e):
    A = 10**-3 * h * l1 * l2 * (o - x) / (0.0821 * (273 + t))
    B = A / e
    C = B * 12 * 60 / 10**6
    ra = 10**4 * C / (l1 * l2)
    return ra


def converter_from_GPerGH_to_GPerM2H(measure, power):
    # 10**5 g/(g*h) -> g/(m2*h); 10**8 mg/(g*h) -> g/(m2*h); 10**11 mcg/(g*h) -> g/(m2*h)
    if power == "micro":
        converted = measure * 3 * 10**11
    elif power == "milli":
        converted = measure * 3 * 10**8
    elif power == "no":
        converted = measure * 3 * 10**5
    elif power == "mcgPerM":
        converted = measure * 3 * 10**5 * 10**6
    else:
        print("Process finished with exit code 1")
    return converted


def converter_from_GPerM2H_to_GPerGH(measure, power):
    if power == "micro":
        converted = measure * 3 * 10**(-11)
    elif power == "milli":
        converted = measure * 3 * 10**(-8)
    elif power == "no":
        converted = measure * 3 * 10**(-5)
    elif power == "mcgPerM":
        converted = measure * 10**6
    else:
        print("Process finished with exit code 1")
    return converted
