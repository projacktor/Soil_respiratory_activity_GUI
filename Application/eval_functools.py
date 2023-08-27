from math import pi


def lab_gkh(x, o, b1, t, d, m, b2, e):
    '''TODO: remake formulas'''
    a_main_var = (((o - x) * b1) / 1_000_000)
    b_main_var = a_main_var * 1013.25 * 273 / ((1013.25 + d) * (273 + t))
    ra = (b_main_var * 44 / (22.4 * e * m * (b2 / 100))) * 10
    return ra
# print(lab_gkh(455.7955, 745.718, 18.5, 25.7, 1013.25, 2.33, 20, 17.5))


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
