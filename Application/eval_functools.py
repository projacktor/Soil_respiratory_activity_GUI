from math import pi


# Function for calculation RA in lab-ry using gas chromatograph
def lab_gkh(x, o, b1, t, d, m, b2, e):
    a = ((o - x) * b1) / 1_000_000
    b = a * d * 273 / (1013.25 * (273 + t))
    ra = (b * 44) / ((22.4 * e) * (m - (b2 / 100)))
    # It returns value in mgCO2*g**(-1)*h**(-1)
    return ra


# Function for calculation RA in lab-ry using titration method
def lab_titr(x, o, m, e):
    ra = 2.2 * ((x - o) / (e * m))
    # It returns value in mgCO2*g**(-1)*h**(-1)
    return ra


# Function for calculation RA in field conditions using CO2 analyzer
def field_co2(x, o, h, d, t, e):
    a = 0.001 * h * ((pi * d**2) / 4) * (o - x) / (0.0821 * (273 + t))
    b = a / e
    c = b * 12 * 60 / 10**-6
    ra = 10**4 * c / ((pi * d**2) / 4)
    # It returns value in gCO2*m**(-2)*h**(-1)
    return ra


# Function for calculation RA in field conditions using gas chromatograph
def field_gkh(x, o, h, l1, l2, t, e):
    a = 10**-3 * h * l1 * l2 * (o - x) / (0.0821 * (273 + t))
    b = a / e
    c = b * 12 * 60 / 10**6
    ra = 10**4 * c / (l1 * l2)
    # It returns value in gCO2*m**(-2)*h**(-1)
    return ra


# Function for converting value from with measure that contains gCO2*g**(-1)*h**(-1) to gCO2*m**(-2)*h**(-1)
def converter_from_GPerGH_to_GPerM2H(measure, power):
    # 10**5 g/(g*h) -> g/(m2*h); 10**8 mg/(g*h) -> g/(m2*h); 10**11 mcg/(g*h) -> g/(m2*h)
    converted = None
    if power == "micro":
        # this condition converts RA in mcgCO2*g**(-1)*h**(-1) to gCO2*m**(-2)*h**(-1)
        converted = measure * 3 * 10**11
    elif power == "milli":
        # this condition converts RA in mcgCO2*g**(-1)*h**(-1) to gCO2*m**(-2)*h**(-1)
        converted = measure * 3 * 10**8
    elif power == "no":
        # this condition converts RA in gCO2*g**(-1)*h**(-1) to gCO2*m**(-2)*h**(-1)
        converted = measure * 3 * 10**5
    elif power == "mcgPerM":
        # this condition converts RA in gCO2*g**(-1)*h**(-1) to mcgCO2*m**(-2)*h**(-1)
        converted = measure * 3 * 10**5 * 10**6
    else:
        print("Process finished with exit code 1")
    return converted


# Function for converting value from gCO2*m**(-2)*h**(-1) to converted one
# that will contain gCO2*g**(-1)*h**(-1) measure
def converter_from_GPerM2H_to_GPerGH(measure, power):
    converted = None
    if power == "micro":
        # this condition converts RA in gCO2*m**(-2)*h**(-1) to mcgCO2*g**(-1)*h**(-1)
        converted = measure * 3 * 10**(-11)
    elif power == "milli":
        # this condition converts RA in gCO2*m**(-2)*h**(-1) to mcgCO2*g**(-1)*h**(-1)
        converted = measure * 3 * 10**(-8)
    elif power == "no":
        # this condition converts RA in gCO2*m**(-2)*h**(-1) to mcgCO2*g**(-1)*h**(-1)
        converted = measure * 3 * 10**(-5)
    else:
        print("Process finished with exit code 1")
    return converted
