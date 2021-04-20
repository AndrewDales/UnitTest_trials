from math import pi, sqrt


def circle_area(r):
    if r < 0:
        raise ValueError("Input must be greater than or equal to zero")
    return pi * (r ** 2)


def solve_quadratic(a, b, c):
    discriminant = b**2 - 4 * a * c
    if discriminant > 0:
        solutions = ((-b + sqrt(discriminant))/(2*a),
                     (-b - sqrt(discriminant))/(2*a))
    elif discriminant == 0:
        solutions = (-b/(2*a*c),)
    else:
        raise ValueError("No real solutions")
    return solutions
