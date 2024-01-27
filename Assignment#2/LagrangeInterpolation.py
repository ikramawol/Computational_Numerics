# Python Implementation for Lagrange Interpolation

# Estimate the natural logarithm of 2 using linear interpolation. First, perform the computation by interpolating between ln 1 = 0 and ln 6 = 1.791759. Then,
# repeat the procedure, but use a smaller interval from ln 1 to ln 4 (1.386294). Note that the
# true value of ln 2 is 0.6931472

# Use a Lagrange interpolating polynomial of the first and second
# order to evaluate ln 2 on the basis of the data given in Example 18.2:
# x0 = 1 f(x0) = 0
# x1 = 4 f(x1) = 1.386294
# x2 = 6 f(x2) = 1.791760

def lagrange_interpolation(x, y, n, xx):
    lagrange_sum = 0

    for i in range(n+1):
        product = y[i]

        for j in range(n+1):
            if i != j:
                product *= (xx - x[j]) / (x[i] - x[j])

        lagrange_sum += product

    return lagrange_sum


x_values = [1, 4, 6]
y_values = [0, 1.386294, 1.791759]
n = len(x_values) - 1

x_value = 2
result = lagrange_interpolation(x_values, y_values, n, x_value)

print("Estimate using Lagrange Interpolation:", result)