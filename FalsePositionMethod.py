# False Position method
def false_position_method(func, a, b, tol=1e-6, max_iter=100):
    iter_count = 0
    while iter_count < max_iter:
        c = (a * func(b) - b * func(a)) / (func(b) - func(a))
        if func(c) == 0:
            break
        elif func(c) * func(a) < 0:
            b = c
        else:
            a = c
        iter_count += 1
    return c

# Finding drag coefficient using False Position method
c_false_position = false_position_method(f, 0.1, 1)

# Display the result
print(f"Drag coefficient using False Position method: {c_false_position:.6f}")
