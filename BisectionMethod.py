import math

# Given values
m = 68.1  # mass in kg
g = 9.8   # acceleration due to gravity in m/s^2
v_target = 40  # target velocity in m/s
t = 10  # time in seconds

# Function representing the equation of motion
def f(c):
    return (g * m / c) * (1 - math.exp(-c / m * t)) - v_target

# Bisection method
def bisection_method(func, a, b, tol=1e-6, max_iter=100):
    iter_count = 0
    while (b - a) / 2 > tol and iter_count < max_iter:
        c = (a + b) / 2
        if func(c) == 0:
            break
        elif func(c) * func(a) < 0:
            b = c
        else:
            a = c
        iter_count += 1
    return c

# Finding drag coefficient using Bisection method
c_bisection = bisection_method(f, 0.1, 1)

# Display the result
print(f"Drag coefficient using Bisection method: {c_bisection:.6f}")
