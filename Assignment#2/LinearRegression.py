# Python Implementation for Linear Regression

def linear_regression(x, y, n):
    sumx = sumy = sumxy = sumx2 = 0
    st = sr = 0

    for i in range(n):
        sumx += x[i]
        sumy += y[i]
        sumxy += x[i] * y[i]
        sumx2 += x[i] ** 2

    xm = sumx / n
    ym = sumy / n

    a1 = (n * sumxy - sumx * sumy) / (n * sumx2 - sumx ** 2)
    a0 = ym - a1 * xm

    for i in range(n):
        st += (y[i] - ym) ** 2
        sr += (y[i] - a1 * x[i] - a0) ** 2

    syx = (sr / (n - 2)) ** 0.5
    r2 = (st - sr) / st

    return a0, a1, syx, r2

# Example usage:
x_values = [1, 2, 3, 4, 5]
y_values = [2, 4, 5, 4, 5]
n = len(x_values)

a0, a1, syx, r2 = linear_regression(x_values, y_values, n)

print("Intercept (a0):", a0)
print("Slope (a1):", a1)
print("Standard Error of Estimate (syx):", syx)
print("Coefficient of Determination (r2):", r2)