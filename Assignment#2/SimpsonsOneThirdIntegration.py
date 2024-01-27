# Python Implementation for simpsons one third integration (1/3)

# Problem Statement. Use Eq. (21.15) to integrate
# f(x) = 0.2 + 25x − 200x 2 + 675x3 − 900x4 + 400x5
# from a = 0 to b = 0.8. Recall that the exact integral is 1.640533. 

def f(x):
    return 0.2 + 25 * x - 200 * x**2 + 675 * x**3 - 900 * x**4 + 400 * x**5

def simpsons_rule(a, b, n):
    h = (b - a) / n
    result = f(a) + f(b)

    for i in range(1, n):
        x = a + i * h
        if i % 2 == 0:
            result += 2 * f(x)
        else:
            result += 4 * f(x)

    result *= h / 3
    return result

a = 0
b = 0.8
n = 1000  

integral_approx = simpsons_rule(a, b, n)

correct_value = 1.640533

print(f"Estimated Integral: {integral_approx}")
print(f"Exact Value for the Integral: {correct_value}")


