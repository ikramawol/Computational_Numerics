# Python Implementation for simpsons three eighth integration (3/8)

# Problem Statement:
# Use Simpson’s 3/8 rule to integrate
# f(x) = 0.2 + 25x − 200x 2 + 675x3 − 900x4 + 400x5
# from a = 0 to b = 0.8. 

def f(x):
    return 0.2 + 25 * x - 200 * x**2 + 675 * x**3 - 900 * x**4 + 400 * x**5

def simpsons_3_8_rule(a, b):
    n = 3
    h = (b - a) / n
    result = f(a) + f(b)

    for i in range(1, n):
        x = a + i * h
        result += 3 * f(x)

    result *= 3 * h / 8
    return result

a = 0
b = 0.8

integral_approx = simpsons_3_8_rule(a, b)

print(f"Estimated Integral: {integral_approx}")
