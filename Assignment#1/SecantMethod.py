import math

# Given values
m = 68.1  # mass in kg
g = 9.8   # acceleration due to gravity in m/s^2
v_target = 40  # target velocity in m/s
t = 10  # time in seconds

# Function representing the equation of motion
def Equ_Motion(c):
    return (g * m / c) * (1 - math.exp(-c / m * t)) - v_target
# Secant method
def secant_method(func, x0, x1, tol=1e-6, max_iter=100):
    iter_count = 0
    while abs(func(x1)) > tol and iter_count < max_iter:
        x2 = x1 - func(x1) * (x1 - x0) / (func(x1) - func(x0))
        x0, x1 = x1, x2
        iter_count += 1
    return x1

# Finding drag coefficient using Secant method
c_secant = secant_method(Equ_Motion, 0.1, 0.2)

# Display the result
print(f"Drag coefficient using Secant method: {c_secant:.6f}")
