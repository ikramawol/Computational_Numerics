import math

# Given values
m = 68.1  # mass in kg
g = 9.8   # acceleration due to gravity in m/s^2
v_target = 40  # target velocity in m/s
t = 10  # time in seconds

# Function representing the equation of motion
def Equ_Motion(c):
    return (g * m / c) * (1 - math.exp(-c / m * t)) - v_target
# Derivative of the function for Newton-Raphson method
def Derivative_f(c):
    return (g * m / c**2) * (m * t * math.exp(-c / m * t) - c) * math.exp(-c / m * t)

# Newton-Raphson method
def newton_raphson_method(func, df, x0, tol=1e-6, max_iter=100):
    iter_count = 0
    x = x0
    while abs(func(x)) > tol and iter_count < max_iter:
        x = x - func(x) / df(x)
        iter_count += 1
    return x

# Finding drag coefficient using Newton-Raphson method
c_newton_raphson = newton_raphson_method(Equ_Motion, Derivative_f, 0.1)

# Display the result
print(f"Drag coefficient using Newton-Raphson method: {c_newton_raphson:.6f}")
