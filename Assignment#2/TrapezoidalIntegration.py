# Python imlementation for Trapezoidal Integration

# Problem Statement. Use Eq. (21.3) to numerically integrate
# f(x) = 0.2 + 25x − 200x 2 + 675x3 − 900x4 + 400x5
# from a = 0 to b = 0.8. Recall from Sec. PT6.2 that the exact value of the integral can be
# determined analytically to be 1.640533.


def f(x):
    return 0.2 + 25 * x - 200 * x**2 + 675 * x**3 - 900 * x**4 + 400 * x**5

def trapezoidal_rule(a, b, n):
    h = (b - a) / n
    result = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        result += f(a + i * h)
    result *= h
    return result

a = 0
b = 0.8
n = 1000  

integral_approx = trapezoidal_rule(a, b, n)

correct_value = 1.640533

print(f"Estimated Integral: {integral_approx}")
print(f"Exact Value for the Integral: {correct_value}")
