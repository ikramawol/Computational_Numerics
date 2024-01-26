# Python Implementaion for Polynomial Regression

def polynomial_regression(x, y, order):
    n = len(x)
    coefficients = [[0 for _ in range(order + 1)] for _ in range(order + 1)]

    for i in range(1, order + 2):
        for j in range(1, i):
            k = i + j - 2
            sum_val = sum(x[l] ** k for l in range(n))

            coefficients[i - 1][j - 1] = sum_val
            coefficients[j - 1][i - 1] = sum_val

    sum_val = 0
    for m in range(1, n + 1):
        sum_val += y[m - 1] * x[m - 1]

    coefficients[order][0] = 2 * sum_val

    return coefficients
