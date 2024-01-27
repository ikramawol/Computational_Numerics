# Python Implementation for Newton's Interpolation

# Estimate the natural logarithm of 2 using linear interpolation. First, perform the computation by interpolating between ln 1 = 0 and ln 6 = 1.791759. Then,
# repeat the procedure, but use a smaller interval from ln 1 to ln 4 (1.386294). Note that the
# true value of ln 2 is 0.6931472.#

# Fit a second-order polynomial to the three points used in Exam ple 18.1:
# x0 = 1 f(x0) = 0
# x1 = 4 f(x1) = 1.386294
# x2 = 6 f(x2) = 1.791759
# Use the polynomial to evaluate ln 2. 

def newton_interpolation(x, y, n, xi):
    fdd = [[0] * (n+1) for _ in range(n+1)]

    for i in range(n+1):
        fdd[i][0] = y[i]

    for j in range(1, n+1):
        for i in range(n-j+1):
            fdd[i][j] = (fdd[i+1][j-1] - fdd[i][j-1]) / (xi[i+j] - xi[i])

    xterm = 1
    yint = fdd[0][0]

    for order in range(1, n+1):
        xterm *= (x - xi[order-1])
        yint += fdd[0][order] * xterm

    return yint


x_values = [1, 6]
y_values = [0, 1.791759]
n = len(x_values) - 1 

x_value = 2
result = newton_interpolation(x_value, y_values, n, x_values)

print("Estimate using Newton's Interpolating Polynomial:", result)


